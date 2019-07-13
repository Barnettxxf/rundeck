import pytest

from rundeck.exceptions import ResponseError


def test_execution_by_project(rd):
    r = rd.get_executions_by_project(rd.list_projects().project_names[-1])

    assert r.data
    assert r.page


def test_execution_by_job(rd):
    r = rd.get_executions_by_job(rd.list_jobs(rd.list_projects().project_names[-1]).job_ids[-1])

    assert r.data
    assert r.page


def test_execution_running_list(rd):
    r = rd.get_execution_running_list(rd.list_projects().project_names[-1])

    assert r.data
    assert r.page


def test_execution_query_metric(rd):
    def func(av):
        r = rd.get_query_metric_of_exection(rd.list_projects().project_names[-1], api_version=av)

        assert r.data
        assert r.query_metric

    with pytest.raises(ResponseError):
        func(19)
    func(29)


def test_execution_info(rd):
    r = rd.get_execution_info(157)

    assert r.data
    assert r.executions


def test_execution_state(rd):
    r = rd.get_execution_state(157)

    assert r.data
    assert r.state
