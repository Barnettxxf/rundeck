from rundeck.utils.crontab import CronTab, crontab_from_rundeck_schedule


def test_get_job_schedules(rd):
    jl = rd.list_jobs('or')
    job_ids = jl.job_ids

    result = {}
    for job_id in job_ids:
        jd = rd.get_job_definition(job_id)

        sc = jd.definition.schedule
        if sc:
            ct = CronTab(crontab_from_rundeck_schedule(sc))
            result[jd.definition.group + ' - ' + jd.definition.name] = ct.schedule(period='year')

    return result


