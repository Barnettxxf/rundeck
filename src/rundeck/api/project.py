from .base import APIBase


class APIProjects(APIBase):

    def list_projects(self):
        endpoint = f'/api/{self.api_version}/projects'
        return self.get_response(endpoint)

    def list_project_resource(self, project_name):
        endpoint = f'/api/{self.api_version}/project/{project_name}/resources'
        return self.get_response(endpoint)

    def get_project_info(self, project_name):
        endpoint = f'/api/{self.api_version}/project/{project_name}'
        return self.get_response(endpoint)
