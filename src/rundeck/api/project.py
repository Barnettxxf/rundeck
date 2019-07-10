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

    def project_archive_export(self, project_name, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/export'
        return self.get_response(endpoint, 'get', params=options)

    def project_archive_export_async(self, project_name, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/export/async'
        return self.get_response(endpoint, data=options)

    def project_archive_export_async_status(self, project_name, options):
        endpoint = f'/api/{self.api_version}/project/{project_name}/export/status/{options.pop("token")}'
        return self.get_response(endpoint, data=options)

    def project_archive_export_async_download(self, project_name, options):
        endpoint = f'/api/{self.api_version}/project/{project_name}/export/download/{options.pop("token")}'
        return self.get_response(endpoint, data=options)

    def project_archive_import(self, project_name, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/import'
        return self.get_response(endpoint, 'put', params=options)

    def history(self, project_name, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/history'
        return self.get_response(endpoint, params=options)
