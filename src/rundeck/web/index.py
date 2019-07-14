import datetime
from collections import defaultdict

from flask.blueprints import Blueprint
from flask import render_template, url_for, current_app as app, g, request

from ..utils.data import get_job_schedules, months, month_fullname
from ..utils.crontab import CronTab, crontab_from_rundeck_schedule, get_monday, get_sunday

bp = Blueprint('index', __name__)


@bp.route('/year')
def year():
    year = {
        'January': {},
        'February': {},
        'March': {},
        'April': {},
        'May': {},
        'June': {},
        'July': {},
        'August': {},
        'September': {},
        'October': {},
        'November': {},
        'December': {},
    }
    scs = get_job_schedules('or', period='year')
    total = 0
    for v in scs.values():
        total += len(v)

    r = defaultdict(dict)
    for k, v in scs.items():
        for e in v:
            if k in r[e.month].keys():
                r[e.month][k] += 1
            else:
                r[e.month][k] = 1

    mapping = {v: month_fullname[k] for k, v in months.items()}
    year.update({mapping[k]: v for k, v in r.items()})

    content = {
        'year': year,
        'total': total,
    }
    return render_template('index.html', **content)


@bp.route('/month')
def month():
    return ''


@bp.route('/timeline/<project>/<group>')
def timeline(project, group):
    repeat = request.args.get('repeat', 0, type=int)
    from rundeck import ExportJobOptions
    o = ExportJobOptions(
        groupPath=group
    )
    r = g.rd.export_jobs(project, o)
    result = []
    if repeat:
        for e in r.exports:
            if e.schedule:
                ct = CronTab(crontab_from_rundeck_schedule(e.schedule))
                start, end = get_monday(), get_sunday()
                while True:
                    sec = ct.next(start)
                    start = start + datetime.timedelta(seconds=sec)
                    if (start - end).days > 0:
                        break
                    export = e.copy()
                    export['next_schedule'] = start
                    result.append(export)
            else:
                e['next_schedule'] = datetime.datetime(datetime.datetime.now().year + 1, 1, 1)
                result.append(e)
        print(result)
    else:
        for e in r.exports:
            if e.schedule:
                ct = CronTab(crontab_from_rundeck_schedule(e.schedule))
                now = datetime.datetime.now()
                sec = ct.next(now)
                ns = now + datetime.timedelta(seconds=sec)
                e['next_schedule'] = ns
            else:
                e['next_schedule'] = datetime.datetime(datetime.datetime.now().year + 1, 1, 1)
        result = r.exports

    content = {
        'items': sorted(result, key=lambda x: x['next_schedule'])
    }
    return render_template('timeline.html', **content)


@bp.route('/timeline/<job>')
def job_timeline(job):
    r = g.rd.get_job_definition(job)
    result = []
    if r.definition.schedule:
        ct = CronTab(crontab_from_rundeck_schedule(r.definition.schedule))
        start, end = get_monday(), get_sunday()
        while True:
            sec = ct.next(start)
            start = start + datetime.timedelta(seconds=sec)
            if (start - end).days > 0:
                break
            export = r.definition.copy()
            export['next_schedule'] = start
            result.append(export)
    else:
        r.definition['next_schedule'] = datetime.datetime(datetime.datetime.now().year + 1, 1, 1)
        result.append(r.definition)
    content = {
        'items': result
    }
    return render_template('timeline.html', **content)


@bp.app_template_filter('next_schedule_date')
def next_schedule_date(value):
    return value.strftime('%Y-%m-%d')


@bp.app_template_filter('next_schedule_time')
def next_schedule_time(value):
    return value.strftime('%H:%M:%S')
