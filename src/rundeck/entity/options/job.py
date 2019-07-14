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
    format = Field(type_=['xml', 'yaml'], default='yaml')
    idlist = Field()
    groupPath = Field()
    jobFilter = Field()


class ImportJobOptions(OptionsBase):
    content = Field()
    fileformat = Field(type_=['xml', 'yaml'], default='yaml')
    dupeOption = Field(type_=['skip', 'create', 'update'], default='create')
    uuidOption = Field(type_=['preserve', 'remove'], default='preserve')


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
    files = Field()
    optionName = Field()
    fileName = Field()


class ListJobUploadedFileOptions(OptionsBase):
    max = Field()
    fileState = Field(type_=['temp', 'deleted', 'expired', 'retained'])


class ImportJobTemplateOptions(OptionsBase):
    description = Field()
    group = Field()
    name = Field()
    filter = Field()
    recipients = Field()
    subject = Field()
    delay = Field()
    retry = Field()
    month = Field()
    hour = Field()
    minute = Field()
    seconds = Field()
    day = Field()
    year = Field()
    command_description = Field()
    exec = Field()
    strategy = Field()
    timeout = Field()
