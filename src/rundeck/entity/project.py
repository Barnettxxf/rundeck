from .base import EntityBase, EntityWithProjectName
from ..api.project import APIProjects
from .item.project import ProjectItem, ResourceItem, InfoItem


class ProjectList(EntityBase):
    api_cls = APIProjects

    def __init__(self, client, api_version=19):
        super().__init__(client, api_version)
        self._data = self.api.list_projects()
        self._result = [ProjectItem(**p) for p in self._data]

    @property
    def projects(self):
        return self._result

    @property
    def project_names(self):
        return [x['name'] for x in self._result]


class ProjectResources(EntityWithProjectName):
    api_cls = APIProjects
    item_cls = ResourceItem
    api_func_name = 'list_project_resource'

    @property
    def resources(self):
        return self._result

    def _init(self, pn, o):
        self._project_name = pn
        self._data = self.api.list_project_resource(pn)
        self._result = [self.item_cls(**x) for x in self._data.values()]


class ProjectInfo(EntityWithProjectName):
    api_cls = APIProjects
    item_cls = InfoItem
    api_func_name = 'get_project_info'

    @property
    def project_info(self):
        return self._result
