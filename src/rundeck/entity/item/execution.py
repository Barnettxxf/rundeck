from .base import Item, Field


class ExecutionPageItem(Item):
    count = Field()
    total = Field()
    offset = Field()
    max = Field()


class ExecutionItem(Item):
    id = Field()
    href = Field()
    permalink = Field()
    status = Field()
    customStatus = Field()
    project = Field()
    user = Field()
    serverUUID = Field()
    date_started = Field()
    date_ended = Field()
    job = Field()
    description = Field()
    argstring = Field()
    successfulNodes = Field()
    executionType = Field()

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id} job={self.job} project={self.project}>'


class ExecutionQueryMetricItem(Item):
    duration = Field()
    total = Field()
    status = Field()

    def __repr__(self):
        return f'{self.__class__.__name__} status={self.status}'


class ExecutionStateItem(Item):
    executionId = Field()
    serverNode = Field()
    nodes = Field()
    executionState = Field()
    updateTime = Field()
    startTime = Field()
    completed = Field()
    endTime = Field()
    allNodes = Field()
    stepCount = Field()
    steps = Field()
    targetNodes = Field()
