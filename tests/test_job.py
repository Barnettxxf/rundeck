from rundeck import JobForecast, JobList, JobMetadata, ExportJob, ListJobOptions
import pytest


def test_job_list(cli):
    r = JobList('or', cli)

    assert r.data
    assert r.jobs
    assert r.project_name

    o = ListJobOptions(groupPath='simple')
    r = JobList('or', cli, options=o)

    assert r.data


def test_export_job(cli):
    r = ExportJob('c5aa2e58-1342-42c4-9350-2493f90a8728', cli)

    assert r.data
    assert r.result


def test_job_metadata(cli):
    r = JobMetadata('c5aa2e58-1342-42c4-9350-2493f90a8728', cli)

    assert r.data
    assert r.result


@pytest.mark.skip('Not support yet')
def test_job_forecast(cli):
    r = JobForecast('c5aa2e58-1342-42c4-9350-2493f90a8728', cli)

    assert r.data
    assert r.forecast
