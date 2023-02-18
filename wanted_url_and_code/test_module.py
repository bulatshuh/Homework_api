import requests


def test_given_url(get_url, get_status_code):
    response = requests.get(get_url)

    assert response.status_code == int(get_status_code), f'Wrong status code, {int(get_status_code)} ' \
                                                         f'is expected'
