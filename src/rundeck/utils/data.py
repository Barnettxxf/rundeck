from .crontab import CronTab, crontab_from_rundeck_schedule
from .. import JobList, ExportJob

month_fullname = {
    'jan': 'January',
    'feb': 'February',
    'mar': 'March',
    'apr': 'April',
    'may': 'May',
    'jun': 'June',
    'jul': 'July',
    'aug': 'August',
    'sep': 'September',
    'oct': 'October',
    'nov': 'November',
    'dec': 'December',
}
months = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
          'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
week = {'sun': 0, 'mon': 1, 'tue': 2, 'wed': 3, 'thu': 4, 'fri': 5,
        'sat': 6}


def get_job_schedules(pn, cli, options=None, api_version=19):
    jl = JobList(pn, cli, options, api_version)
    job_ids = jl.job_ids

    result = {}
    for job_id in job_ids:
        ej = ExportJob(job_id, cli)

        sc = ej.result.schedule
        if sc:
            ct = CronTab(crontab_from_rundeck_schedule(sc))
            result[ej.result.group + ' - ' + ej.result.name] = ct.schedule(period='year')

    return result
