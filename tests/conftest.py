import pytest
from click.testing import CliRunner


@pytest.fixture(scope='function', params=['', 'home'])
def home(request, tmpdir):
    return tmpdir.ensure(request.param, dir=1)


@pytest.fixture(scope='function')
def repo(tmpdir):
    return tmpdir.ensure('repo', dir=1)


@pytest.fixture(scope='function')
def runner():
    return CliRunner()
