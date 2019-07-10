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


class ProjectArchiveImportOption(OptionsBase):
    jobUuidOption = Field()
    importExecutions = Field()
    importConfig = Field()
    importACL = Field()
    importScm = Field()


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
