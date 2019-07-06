from .base import APIBase


class APIResources(APIBase):

    def list_resources(self, project_name, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/resources'
        return self.get_response(endpoint, params=options)

    def get_resource_info(self, project_name, resource, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/resource/{resource}'
        return self.get_response(endpoint, params=options or {'format': 'json'})
