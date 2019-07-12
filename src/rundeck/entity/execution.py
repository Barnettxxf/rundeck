from .base import EntityWithExecId, EntityWithJobId, EntityWithProjectName, Entity
from .item.execution import ExecutionItem, ExecutionPageItem, ExecutionQueryMetricItem, ExecutionStateItem
from ..api import APIExecutions


class _ExecutionListAndPage(Entity):
    _api_cls = APIExecutions
    _api_func_name = None

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


class ExecutionByJob(EntityWithJobId):
    _api_cls = APIExecutions
    _item_cls = ExecutionItem
    _paging_cls = ExecutionPageItem
    _api_func_name = 'list_executions_by_job'

    @property
    def page(self):
        return self._page

    @property
    def executions(self):
        return self._result


class ExecutionByProject(EntityWithProjectName):
    _api_cls = APIExecutions
    _item_cls = ExecutionItem
    _paging_cls = ExecutionPageItem
    _api_func_name = 'list_executions_by_project'

    @property
    def page(self):
        return self._page

    @property
    def executions(self):
        return self._result


class ExecutionRunningList(EntityWithProjectName):
    _api_cls = APIExecutions
    _item_cls = ExecutionItem
    _paging_cls = ExecutionPageItem
    _api_func_name = 'list_running_executions'

    @property
    def page(self):
        return self._page

    @property
    def executions(self):
        return self._result


class ExecutionInfo(EntityWithExecId):
    _api_cls = APIExecutions
    _api_func_name = 'execution_info'
    _item_cls = ExecutionItem

    @property
    def executions(self):
        return self._result


class ExecutionQueryMetric(EntityWithProjectName):
    _api_cls = APIExecutions
    _api_func_name = 'execution_query_metrics'
    _item_cls = ExecutionQueryMetricItem

    @property
    def query_metric(self):
        return self._result


class ExecutionState(EntityWithExecId):
    _api_cls = APIExecutions
    _api_func_name = 'execution_state'
    _item_cls = ExecutionStateItem

    @property
    def state(self):
        return self._result
