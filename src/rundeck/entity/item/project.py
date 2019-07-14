from .base import Item, Field


class ProjectItem(Item):
    name = Field()
    description = Field()
    url = Field()
    label = Field()

    def __repr__(self):
        return f'<{self.__class__.__name__} name={self.name}>'

    __str__ = __repr__


class ResourceItem(Item):
    nodename = Field()
    hostname = Field()
    osFamily = Field()
    osVersion = Field()
    osArch = Field()
    description = Field()
    osName = Field()
    username = Field()
    tags = Field()

    def __repr__(self):
        return f'<{self.__class__.__name__} nodename={self.nodename} hostname={self.hostname}>'

    __str__ = __repr__


class InfoItem(Item):
    name = Field()
    description = Field()
    url = Field()
    config = Field()

    def __repr__(self):
        return f'<{self.__class__.__name__} name={self.name}>'

    __str__ = __repr__


class ProjectArchiveExportAsyncItem(Item):
    token = Field()
    ready = Field()
    percentage = Field()


class ProjectArchiveExportAsyncStatusItem(ProjectArchiveExportAsyncItem):
    pass


class ProjectArchiveImportItem(Item):
    import_status = Field()
    errors = Field()
    execution_errors = Field()
    acl_errors = Field()


class EventsItem(Item):
    starttime = Field()
    endtime = Field()
    title = Field()
    status = Field()
    statusString = Field()
    summary = Field()
    node_summary = Field()
    user = Field()
    date_started = Field()
    date_ended = Field()
    project = Field()
    job = Field()
    execution = Field()
