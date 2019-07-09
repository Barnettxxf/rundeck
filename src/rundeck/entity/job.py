from .base import EntityWithProjectName, EntityWithJobId
from ..api.job import APIJobs
from .item.job import JobListItem, RunJobItem, ImportJobItem, JobForecastItem, JobMetadataItem, ExportJobItem


class JobList(EntityWithProjectName):
    api_cls = APIJobs
    item_cls = JobListItem
    api_func_name = 'list_jobs'

    @property
    def jobs(self):
        return self._result

    @property
    def job_ids(self):
        return [job['id'] for job in self._result]


class RunJob(EntityWithJobId):
    api_cls = APIJobs
    api_func_name = 'run_job'
    item_cls = RunJobItem

    @property
    def state(self):
        return self._result


class ExportJob(EntityWithJobId):
    api_cls = APIJobs
    api_func_name = 'export_jobs'
    item_cls = ExportJobItem

    @property
    def exports(self):
        return self._result


class ImportJob(EntityWithJobId):
    api_cls = APIJobs
    api_func_name = 'import_jobs'
    item_cls = ImportJobItem

    @property
    def result(self):
        return self._result


class JobForecast(EntityWithJobId):
    api_cls = APIJobs
    api_func_name = 'get_job_forecast'
    item_cls = JobForecastItem

    @property
    def forecast(self):
        return self._result


class JobMetadata(EntityWithJobId):
    api_cls = APIJobs
    api_func_name = 'get_job_metadata'
    item_cls = JobMetadataItem

    @property
    def metadata(self):
        return self._result
