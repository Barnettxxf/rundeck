import pytest

from rundeck.client import Rundeck


@pytest.fixture(scope='session')
def rd():
    cli = Rundeck()
    yield cli
    cli.close()
