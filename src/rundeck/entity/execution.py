from .base import EntityBase
from .item.execution import ExecutionItem, ExecutionPageItem, ExecutionQueryMetricItem, ExecutionStateItem
from ..api import APIExecutions


class _ExecutionListAndPage(EntityBase):
    api_cls = APIExecutions
    api_func_name = None

    def __init__(self, itm_id, client, option=None, api_version=19):
        super().__init__(client, api_version)
        self._init(itm_id, option)

    @property
    def page(self):
        return self._page

    @property
    def executions(self):
        return self._result

    def _init(self, itm_id, option):
        self._data = getattr(self.api, self.api_func_name)(itm_id, option)
        self._result = [ExecutionItem(**x) for x in self._data['executions']]
        self._page = ExecutionPageItem(**self._data['paging'])


class ExecutionByJob(_ExecutionListAndPage):
    api_func_name = 'list_executions_by_job'

    def __init__(self, job_id, client, option=None, api_version=19):
        super().__init__(job_id, client, option, api_version)


class ExecutionByProject(_ExecutionListAndPage):
    api_func_name = 'list_executions_by_project'

    def __init__(self, project_name, client, option=None, api_version=19):
        super().__init__(project_name, client, option, api_version)


class ExecutionRunningList(_ExecutionListAndPage):
    api_func_name = 'list_running_executions'

    def __init__(self, project_name, client, option=None, api_version=19):
        super().__init__(project_name, client, option, api_version)


class ExecutionInfo(EntityBase):
    api_cls = APIExecutions

    def __init__(self, exec_id, client, api_version=19):
        super().__init__(client, api_version)
        self._data = self.api.execution_info(exec_id)
        self._result = ExecutionItem(**self._data)

    @property
    def executions(self):
        return self._result


class ExecutionQueryMetric(EntityBase):
    api_cls = APIExecutions

    def __init__(self, project_name, client, api_version=19):
        super().__init__(client, api_version)
        self._data = self.api.execution_query_metrics(project_name)
        self._result = ExecutionQueryMetricItem(**self._data)

    @property
    def query_metric(self):
        return self._result


# TODO 待完成，有点多
class ExecutionState(EntityBase):
    api_cls = APIExecutions

    def __init__(self, exec_id, client, api_version=19):
        super().__init__(client, api_version)
        self._data = self.api.execution_state(exec_id)
        self._result = ExecutionStateItem(**self._data)

    @property
    def state(self):
        return self._result
