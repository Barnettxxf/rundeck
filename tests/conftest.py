import pytest

from rundeck.client import RundeckClient


@pytest.fixture(scope='session')
def cli():
    rundeck_url = 'http://localhost:4440'
    conf = {
        'username': 'admin',
        'password': 'admin',
    }
    cli = RundeckClient(rundeck_url, conf)
    yield cli
    cli.close()
