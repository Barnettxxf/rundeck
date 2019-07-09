from rundeck.entity.options.base import EmptyOptions
from .base import EntityWithProjectName
from ..api.project import APIProjects
from .item.project import ProjectItem, ResourceItem, InfoItem


class ProjectList(EntityWithProjectName):
    api_cls = APIProjects
    item_cls = ProjectItem
    api_func_name = 'list_projects'

    def __init__(self, client, api_version=19):
        super().__init__(client, '', EmptyOptions, api_version)

    @property
    def projects(self):
        return self._result

    @property
    def project_names(self):
        return [x['name'] for x in self._result]

    @property
    def project_name(self):
        raise ValueError(f'{self.__class__.__name__} do not support this attribute yet')


class ProjectResources(EntityWithProjectName):
    api_cls = APIProjects
    item_cls = ResourceItem
    api_func_name = 'list_project_resource'

    @property
    def resources(self):
        return self._result


class ProjectInfo(EntityWithProjectName):
    api_cls = APIProjects
    item_cls = InfoItem
    api_func_name = 'get_project_info'

    @property
    def project_info(self):
        return self._result
