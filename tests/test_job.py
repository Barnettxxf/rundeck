

def test_job_list(rd):
    r = rd.list_jobs('or')

    assert r.data
    assert r.jobs
    assert r.project_name

    from rundeck import ListJobOptions

    o = ListJobOptions(groupPath='simple')
    r = rd.list_jobs('or', o)

    assert r.data


def test_export_jobs(rd):
    from rundeck import ExportJobOptions
    o = ExportJobOptions(
        groupPath='farfetch'
    )
    r = rd.export_jobs(rd.list_projects().project_names[-1], o)

    assert r.data
    assert r.exports[-1].to_yaml()


def test_job_metadata(rd):
    r = rd.get_job_metadata(rd.list_jobs('or').job_ids[-1])

    assert r.data


def test_get_job_definition(rd):
    r = rd.get_job_definition(rd.list_jobs('or').job_ids[-1])
    assert r.data


def test_import_jobs(rd):
    from rundeck.entity.options.job import ImportJobOptions
    from rundeck.utils.template import import_job_tmpl
    o = ImportJobOptions(
        content=import_job_tmpl.substitute(**{
            'description': 'test',
            'group': 'test',
            'name': 'test',
            'filter': '.*',
            'recipients': 'xuxiongfeng@yimian.com.cn',
            'subject': 'test',
            'delay': '1m',
            'retry': '2',
            'month': '*',
            'hour': '*',
            'minute': '0/5',
            'seconds': '0',
            'day': '*',
            'year': '*',
            'command_description': 'test',
            'exec': 'ls',
            'strategy': '',
            'timeout': '2s',
        })
    )
    r = rd.import_jobs('or', o)

    assert r.data
