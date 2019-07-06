from .base import EntityBase, EntityWithProjectName
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


class RunJob(EntityBase):
    api_cls = APIJobs

    def __init__(self, job_id, client, options, api_version=19):
        super().__init__(client, api_version)
        self._data = self.api.run_job(job_id, options)
        self._result = RunJobItem(**self.data)

    @property
    def state(self):
        return self._result


class ExportJob(EntityBase):
    api_cls = APIJobs

    def __init__(self, job_id, client, options=None, api_version=19):
        super().__init__(client, api_version)
        self._data = self.api.export_job(job_id, options)
        self._result = ExportJobItem(**self._data[0])

    @property
    def result(self):
        return self._result


class ImportJob(EntityBase):
    api_cls = APIJobs

    def __init__(self, job_id, client, options, api_version=19):
        super().__init__(client, api_version)
        self._data = self.api.import_job(job_id, options)
        self._result = ImportJobItem(**self._data)

    @property
    def result(self):
        return self._result


class JobForecast(EntityBase):
    api_cls = APIJobs

    def __init__(self, job_id, client, options=None, api_version=19):
        super().__init__(client, api_version)
        self._data = self.api.get_job_forecast(job_id, options)
        self._result = JobForecastItem(**self._data)

    @property
    def forecast(self):
        return self._result


class JobMetadata(EntityBase):
    api_cls = APIJobs

    def __init__(self, job_id, client, options=None, api_version=19):
        super().__init__(client, api_version)
        self._data = self.api.get_job_metadata(job_id, options)
        self._result = JobMetadataItem(**self._data)

    @property
    def result(self):
        return self._result
