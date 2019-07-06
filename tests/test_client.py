"""
Author: xuxiongfeng
Date: 2019-07-05 15:57
Usage: 
"""
import pytest

from rundeck.client import RundeckClient
from rundeck.error import AuthFailError

rundeck_url = 'http://localhost:4440'


def test_auth_succeed():
    conf = {
        'username': 'admin',
        'password': 'admin',
    }
    cli = RundeckClient(rundeck_url, conf)
    list_projects = '/api/19/projects'
    cli.get(list_projects)
    cli.close()


def test_auth_fail():
    conf = {
        'username': 'admin',
        'password': 'admi',
    }
    cli = RundeckClient(rundeck_url, conf)
    with pytest.raises(AuthFailError):
        list_projects = '/api/19/projects'
        cli.get(list_projects)
