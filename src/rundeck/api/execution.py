from .base import APIBase


class APIExecutions(APIBase):

    def list_executions_by_project(self, project_name, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/executions'
        return self.get_response(endpoint, params=options)

    def list_executions_by_job(self, job_id, options=None):
        endpoint = f'/api/{self.api_version}/job/{job_id}/executions'
        return self.get_response(endpoint, params=options)

    def list_running_executions(self, project_name='*', option=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/executions/running'
        return self.get_response(endpoint)

    def execution_info(self, execution_id, options=None):
        endpoint = f'/api/{self.api_version}/execution/{execution_id}'
        return self.get_response(endpoint)

    def execution_query_metrics(self, project_name=None, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/executions/metrics' \
            if project_name else f'/api/{self.api_version}/executions/metrics'
        return self.get_response(endpoint, params=options)

    def execution_state(self, execution_id, options=None):
        endpoint = f'/api/{self.api_version}/execution/{execution_id}/state'
        return self.get_response(endpoint)
