from .base import EntityWithProjectName, EntityWithJobId
from ..api.job import APIJobs
from .item.job import JobListItem, RunJobItem, ImportJobItem, JobForecastItem, JobMetadataItem, ExportJobItem


class JobList(EntityWithProjectName):
    _api_cls = APIJobs
    _item_cls = JobListItem
    _api_func_name = 'list_jobs'

    @property
    def jobs(self):
        return self._result

    @property
    def job_ids(self):
        return [job['id'] for job in self._result]


class RunJob(EntityWithJobId):
    _api_cls = APIJobs
    _api_func_name = 'run_job'
    _item_cls = RunJobItem

    @property
    def state(self):
        return self._result


class ExportJob(EntityWithProjectName):
    _api_cls = APIJobs
    _api_func_name = 'export_jobs'
    _item_cls = ExportJobItem

    @property
    def exports(self):
        return self._result


class ImportJob(EntityWithProjectName):
    _api_cls = APIJobs
    _api_func_name = 'import_jobs'
    _item_cls = ImportJobItem

    @property
    def result(self):
        return self._result


class JobForecast(EntityWithJobId):
    _api_cls = APIJobs
    _api_func_name = 'get_job_forecast'
    _item_cls = JobForecastItem

    @property
    def forecast(self):
        return self._result


class JobMetadata(EntityWithJobId):
    _api_cls = APIJobs
    _api_func_name = 'get_job_metadata'
    _item_cls = JobMetadataItem

    @property
    def metadata(self):
        return self._result
