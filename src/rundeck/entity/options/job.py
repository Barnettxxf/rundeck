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
