from collections import defaultdict

from flask.blueprints import Blueprint
from flask import render_template, url_for, current_app as app, g

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
    scs = get_job_schedules('or')
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


@bp.route('/timeline')
def timeline():
    content = {

    }
    return render_template('timeline.html', **content)