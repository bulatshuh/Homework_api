import pytest


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://ya.ru',
                     help="Enter url to send request")

    parser.addoption('--status_code', action='store', default='200',
                     help="Enter expected status code")


@pytest.fixture(scope='session')
def get_url(request):
    user_url = request.config.getoption('url')
    yield user_url


@pytest.fixture(scope='session')
def get_status_code(request):
    user_status_code = request.config.getoption('status_code')
    yield user_status_code
