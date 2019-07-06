import warnings

from crontab import CronTab as CT
from datetime import timedelta, datetime

warnings.filterwarnings('ignore')

__all__ = ['crontab_from_rundeck_schedule', 'format_crontab', 'CronTab']


def get_start_and_end(now=None, period='day'):
    if now:
        if isinstance(now, datetime):
            now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            raise ValueError('now must be None or datetime.datetime object, got %s' % type(now))

    start = now or datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end = now or datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    _one_day = timedelta(days=1)

    if period == 'day':
        return start, end
    elif period == 'week':
        while start.weekday() != 0:
            start -= _one_day
        while end.weekday() != 6:
            end -= _one_day
        return start, end
    elif period == 'month':
        return start.replace(day=1), start.replace(month=start.month + 1, day=1) - _one_day
    elif period == 'year':
        return start.replace(month=1, day=1), end.replace(month=12, day=31)
    else:
        raise ValueError('Not support %s, must in [day, week, month year]' % period)


def crontab_from_rundeck_schedule(schedule: dict):
    return format_crontab(**dict(
        year=schedule['year'],
        month=schedule['month'],
        dayofmonth=schedule['dayofmonth']['day'] if schedule.get('dayofmonth', '') else '?',
        dayofweek=schedule['weekday']['day'] if schedule.get('weekday', '') else '?',
        hour=schedule['time']['hour'],
        minute=schedule['time']['minute'],
        seconds=schedule['time']['seconds'],
    ))


def format_crontab(year='*', month='*', dayofmonth='?', dayofweek='?', hour='*', minute='*', seconds='*'):
    return f'{seconds} {minute} {hour} {dayofmonth} {month} {dayofweek} {year}'


class CronTab(CT):

    def schedule(self, now=None, period='day', only_count=False):
        start, end = get_start_and_end(now, period)
        result = []
        count = 0
        while True:
            sec = self.next(start)
            start = start + timedelta(seconds=sec)
            if (start - end).days > 0:
                break

            if not only_count:
                result.append(start)

            count += 1

        if only_count:
            return count

        return result
