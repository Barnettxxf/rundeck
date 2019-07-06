import datetime
import queue
from functools import partial
from queue import Queue
from collections import ChainMap

import requests

from .error import AuthFailError


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
        rsp = self._session.post(self._base_url + '/j_security_check', headers=self.headers, data={
            'j_username': self.config['username'],
            'j_password': self.config['password'],
        })

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
