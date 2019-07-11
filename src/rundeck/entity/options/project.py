from .base import OptionsBase, Field


class ProjectArchiveExportOptions(OptionsBase):
    executionIds = Field()
    exportAll = Field(type_=bool)
    exportJobs = Field(type_=bool)
    exportExecutions = Field(type_=bool)
    exportConfigs = Field(type_=bool)
    exportReadmes = Field(type_=bool)
    exportAcls = Field(type_=bool)
    exportScm = Field(type_=bool)


class ProjectArchiveExportAsyncOptions(OptionsBase):
    token = Field()


class ProjectArchiveExportAsyncDownloadOptions(ProjectArchiveExportAsyncOptions):
    pass


class ProjectArchiveImportOption(OptionsBase):
    jobUuidOption = Field(type_=['preserve', 'remove'])
    importExecutions = Field(type_=bool)
    importConfig = Field(type_=bool)
    importACL = Field(type_=bool)
    importScm = Field(type_=bool)
    files = Field(type_=dict)


class History(OptionsBase):
    jobIdFilter = Field()
    reportIdFilter = Field()
    userFilter = Field()
    statFilter = Field()
    jobListFilter = Field()
    excludeJobListFilter = Field()
    recentFilter = Field()
    begin = Field()
    end = Field()
    max = Field()
    offset = Field()
