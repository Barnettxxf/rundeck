import pytest
from rundeck import ExecutionQueryMetric, ExecutionInfo, ExecutionByJob, ExecutionByProject, ExecutionState, \
    ExecutionRunningList
from rundeck.error import ResponseError


def test_execution_by_project(cli):
    r = ExecutionByProject('or', cli)

    assert r.data
    assert r.executions
    assert r.page


def test_execution_by_job(cli):
    r = ExecutionByJob('c5aa2e58-1342-42c4-9350-2493f90a8728', cli)

    assert r.data
    assert r.executions
    assert r.page


def test_execution_running_list(cli):
    r = ExecutionRunningList('or', cli)

    assert r.data
    assert r.executions
    assert r.page


def test_execution_query_metric(cli):
    def func(av):
        r = ExecutionQueryMetric('or', cli, api_version=av)

        assert r.data
        assert r.query_metric

    with pytest.raises(AssertionError):
        func(19)
    func(29)


def test_execution_info(cli):
    r = ExecutionInfo('157', cli)

    assert r.data
    assert r.executions


def test_execution_state(cli):
    r = ExecutionState('157', cli)

    assert r.data
    assert r.state
