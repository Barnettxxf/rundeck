from .base import APIBase


class APIJobs(APIBase):

    def list_jobs(self, project_name: str, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/jobs'
        return self.get_response(endpoint, params=options)

    def run_job(self, job_id: str, options: dict):
        endpoint = f'/api/{self.api_version}/job/{job_id}'
        return self.get_response(endpoint, json=options)

    def retry_job(self, job_id: str, exec_id: str, options: dict):
        endpoint = f'/api/{self.api_version}/job/{job_id}/retry/{exec_id}'
        headers = options.pop('headers', {})
        headers['Content-Type'] = 'application/json'
        return self.get_response(endpoint, 'post', headers=headers, json=options)

    def export_job(self, job_id: str, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}'
        return self.get_response(endpoint, params=options or {'format': 'yaml'})

    def import_job(self, project_name: str, options: dict):
        endpoint = f'/api/{self.api_version}/project/{project_name}/jobs/import'
        headers = options.pop('headers', {})
        headers['Content-Type'] = 'application/yaml'
        content = options.pop('content')
        return self.get_response(endpoint, 'post', headers=headers, params=options, data=content)

    def get_job_forecast(self, job_id: str, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}/forecast'
        return self.get_response(endpoint, params=options)

    def get_job_metadata(self, job_id, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}/info'
        return self.get_response(endpoint)
