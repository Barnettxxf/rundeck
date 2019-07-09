from .base import APIBase


class APIProjects(APIBase):

    def list_projects(self, project_name=None, options=None):
        endpoint = f'/api/{self.api_version}/projects'
        return self.get_response(endpoint)

    def list_project_resource(self, project_name, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/resources'
        return self.get_response(endpoint)

    def get_project_info(self, project_name, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}'
        return self.get_response(endpoint)
