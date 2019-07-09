from ..item.base import Field
from .base import OptionsBase


class ListJobOptions(OptionsBase):
    idlist = Field()
    groupPath = Field()
    jobFilter = Field()
    jobExactFilter = Field()
    groupPathExact = Field()
    scheduledFilter = Field(type_=bool)
    serverNodeUUIDFilter = Field()


class RunJobOptions(OptionsBase):
    argString = Field()
    loglevel = Field()
    asUser = Field()
    filter = Field()
    runAtTime = Field()


class RetryJobOptions(OptionsBase):
    argString = Field()
    loglevel = Field()
    asUser = Field()
    failedNodes = Field(type_=bool)


class ExportJobOptions(OptionsBase):
    format = Field()
    idlist = Field()
    groupPath = Field()
    jobFilter = Field()


class ImportJobOptions(OptionsBase):
    content = Field()
    fileformat = Field()
    dupeOption = Field()
    uuidOption = Field()


class JobForecastOptions(OptionsBase):
    time = Field()
    max = Field()


class DeleteJobsOptions(OptionsBase):
    ids = Field()
    idlist = Field()


class BulkToggleJobExecutionOptions(DeleteJobsOptions):
    toggle = Field()


class BulkToggleJobScheduleOptions(BulkToggleJobExecutionOptions):
    pass


class UploadJobOptionFileOptions(OptionsBase):
    file = Field()
    optionName = Field()
    fileName = Field()


class ListJobUploadedFileOptions(OptionsBase):
    max = Field()
    fileState = Field(type_=['temp', 'deleted', 'expired', 'retained'])
