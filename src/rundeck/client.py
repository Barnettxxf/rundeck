import datetime
import queue
from functools import partial
from queue import Queue
from collections import ChainMap

import requests

from .exceptions import AuthFailError


class BaseClient:
    headers = {'Accept': 'application/json'}

    def __init__(self, url, config):
        self._base_url = url
        self.config = config
        self._session = requests.Session()
        self.timeout = datetime.timedelta(minutes=30)
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self._is_auth = False

    def auth(self):
        if not self.config['token']:
            rsp = self._session.post(self._base_url + '/j_security_check', headers=self.headers, data={
                'j_username': self.config['username'],
                'j_password': self.config['password'],
            })
        else:
            headers = self.headers.copy()
            headers.update({
                'X-Rundeck-Auth-Token': self.config['token']
            })
            rsp = self._session.post(self._base_url + '/api/1/projects', headers=headers)

        if 'Invalid username and password' in rsp.text:
            raise AuthFailError('Invalid username and password')

        self._is_auth = True

    @property
    def session(self):
        if not self._is_auth:
            self.auth()
        return self._session

    def close(self):
        self._session.close()

    @property
    def is_timeout(self):
        if datetime.datetime.now() - self.updated_at > self.timeout:
            return True
        return False

    def get(self, endpoint, **kwargs):
        kwargs = self._set_headers(kwargs)
        return self.session.get(self._base_url + endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        kwargs = self._set_headers(kwargs)
        return self.session.post(self._base_url + endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        kwargs = self._set_headers(kwargs)
        return self.session.put(self._base_url + endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        kwargs = self._set_headers(kwargs)
        return self.session.delete(self._base_url + endpoint, **kwargs)

    def _set_headers(self, kwargs):
        headers = kwargs.pop('headers', {})
        kwargs['headers'] = ChainMap(headers, self.headers)
        return kwargs

    def __html__(self):
        return '<rundeck client>'


class RundeckClient:

    def __init__(self, url, config):
        self._base_url = url
        self.config = config
        self._client_queue = Queue()
        self.timeout = datetime.timedelta(minutes=30)
        self._close = False

    def _get_client(self):
        return BaseClient(self._base_url, self.config)

    @property
    def client(self):
        while True:
            try:
                _client = self._client_queue.get_nowait()
            except queue.Empty:
                _client = self._get_client()

            if _client.is_timeout:
                _client.close()
                del _client
                continue

            _client.updated_at = datetime.datetime.now()
            break

        return _client

    def __getattr__(self, item):
        return partial(self.__wrapfunc__, item)

    def __wrapfunc__(self, funcname, *args, **kwargs):
        _client = self.client
        try:
            func = getattr(_client, funcname)
            return func(*args, **kwargs)
        except Exception as e:
            raise e
        finally:
            self.release(_client)

    def release(self, client):
        self._client_queue.put_nowait(client)

    def close(self):
        assert not self._close, 'pool has already closed'
        while not self._client_queue.empty():
            _client = self._client_queue.get_nowait()
            _client.close()
        self._close = True


class Rundeck:

    def __init__(self, server='localhost', protocol='http', username='admin', password='admin', token=None):
        self.url = '://'.join([protocol, server])
        self.config = {
            'username': username,
            'password': password,
            'token': token
        }

        self.cli = RundeckClient(self.url, self.config)

    @property
    def token(self):
        return self.config['token']

    @token.setter
    def token(self, t):
        self.config['token'] = t

    @token.deleter
    def token(self):
        self.config['token'] = None

    def list_tokens(self, user=None, **kwargs):
        from .entity.token import ListTokens
        return ListTokens(self.cli, user, **kwargs)

    def get_token(self, token_id, **kwargs):
        from .entity.token import GetToken
        return GetToken(self.cli, token_id, **kwargs)

    def create_token(self, user=None, **kwargs):
        from .entity.token import CreateToken
        return CreateToken(self.cli, user, **kwargs)

    def delete_token(self, token_id, **kwargs):
        from .entity.token import DeleteToken
        return DeleteToken(self.cli, token_id, **kwargs)

    def create_project(self, options, **kwargs):
        from .entity.project import ProjectCreation
        return ProjectCreation(self.cli, options, **kwargs)

    def list_projects(self, **kwargs):
        from .entity.project import ProjectList
        return ProjectList(self.cli, **kwargs)

    def list_project_resource(self, project_name, **kwargs):
        from .entity.project import ProjectResources
        return ProjectResources(self.cli, project_name, **kwargs)

    def project_info(self, project_name, **kwargs):
        from .entity.project import ProjectInfo
        return ProjectInfo(self.cli, project_name, **kwargs)

    def export_project(self, project_name, options=None, **kwargs):
        from .entity.project import ProjectArchiveExport
        return ProjectArchiveExport(self.cli, project_name, options, **kwargs)

    def export_project_async(self, project_name, options=None, **kwargs):
        from .entity.project import ProjectArchiveExportAsync
        return ProjectArchiveExportAsync(self.cli, project_name, options, **kwargs)

    def get_status_of_export_async(self, project_name, options, **kwargs):
        from .entity.project import ProjectArchiveExportAsyncStatus
        return ProjectArchiveExportAsyncStatus(self.cli, project_name, options, **kwargs)

    def download(self, project_name, options, **kwargs):
        from .entity.project import ProjectArchiveExportAsyncDownload
        return ProjectArchiveExportAsyncDownload(self.cli, project_name, options, **kwargs)

    def import_project(self, project_name, options, **kwargs):
        from .entity.project import ProjectArchiveImport
        return ProjectArchiveImport(self.cli, project_name, options, **kwargs)

    def history(self, project_name, options=None, **kwargs):
        from .entity.project import ListHistory
        return ListHistory(self.cli, project_name, options, **kwargs)

    def list_jobs(self, project_name, options=None, **kwargs):
        from .entity.job import JobList
        return JobList(self.cli, project_name, options, **kwargs)

    def run_job(self, job_id, options=None, **kwargs):
        from .entity.job import RunJob
        return RunJob(self.cli, job_id, options, **kwargs)

    def export_jobs(self, project_name, options=None, **kwargs):
        from .entity.job import ExportJob
        return ExportJob(self.cli, project_name, options, **kwargs)

    def import_jobs(self, project_name, options=None, **kwargs):
        from .entity.job import ImportJob
        return ImportJob(self.cli, project_name, options, **kwargs)

    def get_job_metadata(self, job_id, options=None, **kwargs):
        from .entity.job import JobMetadata
        return JobMetadata(self.cli, job_id, options, **kwargs)

    def get_job_definition(self, job_id, **kwargs):
        from .entity.job import JobDefinition
        return JobDefinition(self.cli, job_id, **kwargs)

    def get_executions_by_job(self, job_id, options=None, **kwargs):
        from .entity.execution import ExecutionByJob
        return ExecutionByJob(self.cli, job_id, options, **kwargs)

    def get_executions_by_project(self, project_name, options=None, **kwargs):
        from .entity.execution import ExecutionByProject
        return ExecutionByProject(self.cli, project_name, options, **kwargs)

    def get_execution_running_list(self, project_name='*', **kwargs):
        from .entity.execution import ExecutionRunningList
        return ExecutionRunningList(self.cli, project_name, **kwargs)

    def get_execution_info(self, exec_id, **kwargs):
        from .entity.execution import ExecutionInfo
        return ExecutionInfo(self.cli, exec_id, **kwargs)

    def get_query_metric_of_exection(self, project_name=None, options=None, **kwargs):
        from .entity.execution import ExecutionQueryMetric
        return ExecutionQueryMetric(self.cli, project_name, options, **kwargs)

    def get_execution_state(self, exec_id, **kwargs):
        from .entity.execution import ExecutionState
        return ExecutionState(self.cli, exec_id, **kwargs)
