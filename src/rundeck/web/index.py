import datetime
from collections import defaultdict

from flask.blueprints import Blueprint
from flask import render_template, url_for, current_app as app, g

from ..client import RundeckClient
from ..utils.data import get_job_schedules, months, month_fullname

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
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
    scs = get_job_schedules('or', g.rundeckcli)
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


@bp.before_app_request
def add_rundeckcli():
    if not g.get('rundeckcli'):
        username = app.config['RUNDECK_USERNAME']
        password = app.config['RUNDECK_PASSWORD']
        url = app.config['RUNDECK_URL']
        g.rundeckcli = RundeckClient(url, {'username': username, 'password': password})


@bp.teardown_app_request
def add_close_rundeckcli(vale):
    rundeckcli = g.pop('rundeckcli', None)
    if rundeckcli:
        rundeckcli.close()
