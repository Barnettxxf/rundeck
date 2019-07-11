from .base import APIBase


class APIJobs(APIBase):

    def list_jobs(self, project_name: str, options: dict = None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/jobs'
        return self.get_response(endpoint, params=options)

    def run_job(self, job_id: str, options: dict = None):
        endpoint = f'/api/{self.api_version}/job/{job_id}'
        return self.get_response(endpoint, json=options)

    def retry_job(self, job_id: str, exec_id: str, options: dict = None):
        endpoint = f'/api/{self.api_version}/job/{job_id}/retry/{exec_id}'
        headers = options.pop('headers', {})
        headers['Content-Type'] = 'application/json'
        return self.get_response(endpoint, 'post', headers=headers, json=options)

    def export_jobs(self, job_id: str, options: dict = None):
        endpoint = f'/api/{self.api_version}/job/{job_id}'
        return self.get_response(endpoint, params=options or {'format': 'yaml'})

    def import_jobs(self, project_name: str, options: dict):
        endpoint = f'/api/{self.api_version}/project/{project_name}/jobs/import'
        headers = options.pop('headers', {})
        headers['Content-Type'] = 'application/yaml'
        content = options.pop('content')
        return self.get_response(endpoint, 'post', headers=headers, params=options, data=content)

    def get_job_definition(self, job_id: str, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}'
        return self.get_response(endpoint, params=options or {'format': 'yaml'})

    def delete_job(self, job_id, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}'
        return self.get_response(endpoint, 'delete')

    def bulk_delete_job(self, options: dict):
        endpoint = f'/api/{self.api_version}/jobs/delete'
        return self.get_response(endpoint, 'post', data=options)

    def enable_job_execution(self, job_id, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}/execution/enable'
        return self.get_response(endpoint, 'post')

    def disable_job_execution(self, job_id, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}/execution/disable'
        return self.get_response(endpoint, 'post')

    def enable_job_scheduling(self, job_id, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}/schedule/enable'
        return self.get_response(endpoint, 'post')

    def disable_job_scheduling(self, job_id, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}/schedule/disable'
        return self.get_response(endpoint, 'post')

    def bulk_toggle_job_execution(self, options=None):
        toggle = options and options.pop('toggle', 'enable') if options else 'enable'
        endpoint = f'/api/{self.api_version}/jobs/execution/{toggle}'
        return self.get_response(endpoint, 'post', data=options)

    def bulk_toggle_job_schedule(self, options=None):
        toggle = options and options.pop('toggle', 'enable') if options else 'enable'
        endpoint = f'/api/{self.api_version}/jobs/schedule/{toggle}'
        return self.get_response(endpoint, 'post', data=options)

    def get_job_metadata(self, job_id, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}/info'
        return self.get_response(endpoint)

    def upload_job_option_file(self, job_id, options: dict):
        files = options.pop('files')
        headers = options.pop('headers', {'Content-Type': 'octet/stream'})
        endpoint = f'api/{self.api_version}/job/{job_id}/input/file'
        return self.get_response(endpoint, 'post', headers=headers, files=files, params=options)

    def list_job_uploaded_file(self, job_id, options: dict):
        endpoint = f'/api/{self.api_version}/job/{job_id}/input/files'
        return self.get_response(endpoint, data=options)

    def get_job_forecast(self, job_id: str, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}/forecast'
        return self.get_response(endpoint, params=options)
