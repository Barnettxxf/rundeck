from .base import APIBase


class APIProjects(APIBase):

    def create_project(self, project_name=None, options=None):
        endpoint = f'/api/{self.api_version}/projects'
        headers = options.pop('headers', {'Content-Type': 'application/json'})
        return self.get_response(endpoint, 'post', headers=headers, json=options)

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
        return self.get_response(endpoint, params=options)

    def project_archive_export_async_status(self, project_name, options):
        endpoint = f'/api/{self.api_version}/project/{project_name}/export/status/{options["token"]}'
        return self.get_response(endpoint)

    def project_archive_export_async_download(self, project_name, options):
        endpoint = f'/api/{self.api_version}/project/{project_name}/export/download/{options["token"]}'
        return self.get_response(endpoint)

    def project_archive_import(self, project_name, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/import'
        headers = options.pop('headers', {'Content-Type': 'application/zip'})
        file = options.pop('file')
        return self.get_response(endpoint, 'put', data=file, headers=headers, params=options)

    def history(self, project_name, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}/history'
        return self.get_response(endpoint, params=options)

    def delete_project(self, project_name, options=None):
        endpoint = f'/api/{self.api_version}/project/{project_name}'
        return self.get_response(endpoint, 'delete')
