from rundeck.entity.options.base import EmptyOptions
from .base import EntityWithProjectName
from ..api.project import APIProjects
from .item.project import ProjectItem, ResourceItem, InfoItem, EventsItem, ProjectArchiveExportAsyncItem, \
    ProjectArchiveExportAsyncStatusItem, ProjectArchiveImportItem


class ProjectCreation(EntityWithProjectName):
    _api_cls = APIProjects
    _item_cls = InfoItem
    _api_func_name = 'create_project'

    def __init__(self, client, options, api_version=19):
        super().__init__(client, '', options, api_version)

    @property
    def project_info(self):
        return self._result


class ProjectList(EntityWithProjectName):
    _api_cls = APIProjects
    _item_cls = ProjectItem
    _api_func_name = 'list_projects'

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
    _api_cls = APIProjects
    _item_cls = ResourceItem
    _api_func_name = 'list_project_resource'

    @property
    def resources(self):
        return self._result


class ProjectInfo(EntityWithProjectName):
    _api_cls = APIProjects
    _item_cls = InfoItem
    _api_func_name = 'get_project_info'

    @property
    def project_info(self):
        return self._result


class ProjectArchiveExport(EntityWithProjectName):
    _api_cls = APIProjects
    _api_func_name = 'project_archive_export'

    @property
    def zip_stream(self):
        return self._result


class ProjectArchiveExportAsync(EntityWithProjectName):
    _api_cls = APIProjects
    _item_cls = ProjectArchiveExportAsyncItem
    _api_func_name = 'project_archive_export_async'

    @property
    def status(self):
        return self._result


class ProjectArchiveExportAsyncStatus(EntityWithProjectName):
    _api_cls = APIProjects
    _item_cls = ProjectArchiveExportAsyncStatusItem
    _api_func_name = 'project_archive_export_async_status'

    @property
    def status(self):
        return self._result

    def refresh(self):
        self._init(self._itm_id, self.options)
        return self.status


class ProjectArchiveExportAsyncDownload(EntityWithProjectName):
    _api_cls = APIProjects
    _api_func_name = 'project_archive_export_async_download'

    @property
    def zip_stream(self):
        return self._result


class ProjectArchiveImport(EntityWithProjectName):
    _api_cls = APIProjects
    _item_cls = ProjectArchiveImportItem
    _api_func_name = 'project_archive_import'

    @property
    def status(self):
        return self._result


class ListHistory(EntityWithProjectName):
    _api_cls = APIProjects
    _item_cls = EventsItem
    _api_func_name = 'history'
    _result_key = 'events'

    @property
    def events(self):
        return self._result
