from .base import OptionsBase, Field


class ExecutionQueryMetricOptions(OptionsBase):
    max = Field()
    offset = Field()


class ExecutionOptions(ExecutionQueryMetricOptions):
    status = Field(type_=['succeeded', 'failed', 'aborted', 'running'])


class ExecutionQueryOptions(ExecutionQueryMetricOptions):
    statusFilter = Field()
    abortedbyFilter = Field()
    userFilter = Field()
    recentFilter = Field()
    begin = Field()
    end = Field()
    olderFilter = Field()
    jobIdListFilter = Field()
    excludeJobIdListFilter = Field()
    jobListFilter = Field()
    excludeJobListFilter = Field()
    groupPath = Field()
    groupPathExact = Field()
    excludeGroupPath = Field()
    excludeGroupPathExact = Field()
    jobFilter = Field()
    excludeJobFilter = Field()
    jobExactFilter = Field()
    excludeJobExactFilter = Field()
    executionTypeFilter = Field()
