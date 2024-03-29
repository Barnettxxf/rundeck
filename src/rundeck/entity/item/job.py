import yaml

from .base import Field, Item


class JobListItem(Item):
    id = Field()
    name = Field()
    group = Field()
    project = Field()
    description = Field()
    href = Field()
    permalink = Field()
    scheduled = Field()
    scheduleEnabled = Field()
    enabled = Field()

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id} name={self.name}>'

    __str__ = __repr__


class RunJobItem(Item):
    loglevel = Field()
    asUser = Field()
    filter = Field()
    runAtTime = Field()
    options = Field()


class ImportJobItem(Item):
    succeeded = Field()
    failed = Field()
    skipped = Field()


class JobForecastItem(Item):
    id = Field()
    name = Field()
    project = Field()
    href = Field()
    futureScheduledExecutions = Field()
    scheduleEnabled = Field()
    scheduled = Field()
    enabled = Field()
    permalink = Field()
    group = Field()
    description = Field()

    def __repr__(self):
        return f'<{self.__class__.__name__} name={self.name}>'

    __str__ = __repr__


class JobMetadataItem(Item):
    id = Field()
    name = Field()
    group = Field()
    project = Field()
    description = Field()
    href = Field()
    permalink = Field()
    scheduled = Field()
    scheduleEnabled = Field()
    enabled = Field()
    nextScheduledExecution = Field()
    averageDuration = Field()

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id} name={self.name}>'

    __str__ = __repr__


class ExportJobItem(Item):
    id = Field()
    uuid = Field()
    name = Field()
    group = Field()
    description = Field()
    schedule = Field()
    options = Field()
    defaultTab = Field()
    executionEnabled = Field()
    loglevel = Field()
    loglimit = Field()
    loglimitAction = Field()
    maxMultipleExecutions = Field()
    nodeFilterEditable = Field()
    notification = Field()
    notifyAvgDurationThreshold = Field()
    retry = Field()
    scheduleEnabled = Field()
    sequence = Field()
    timeout = Field()

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id} name={self.name}>'

    __str__ = __repr__

    def to_yaml(self):
        return yaml.safe_dump([dict(self), ])


class DeleteJobsItem(Item):
    requestCount = Field()
    allsuccessful = Field()
    succeeded = Field()
    failed = Field()


class BulkToggleJobExecutionItem(DeleteJobsItem):
    enabled = Field()


class BulkToggleJobScheduleItem(DeleteJobsItem):
    pass


class UploadJobOptionFileItem(Item):
    total = Field()
    options = Field()


class ListJobUploadedFileItem(Item):
    id = Field()
    user = Field()
    fileState = Field()
    sha = Field()
    jobId = Field()
    dateCreated = Field()
    serverNodeUUID = Field()
    fileName = Field()
    expirationDate = Field()
    execId = Field()

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id} user={self.user}>'

    __str__ = __repr__
