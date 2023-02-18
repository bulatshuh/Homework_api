import requests
import pytest
from test_data import TestData


def test_all_breweries_metadata():
    response = requests.get('https://api.openbrewerydb.org/breweries/meta')

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_dict = response.json()

    assert 'total' in response_dict, 'No "total" key in response'
    assert 'page' in response_dict, 'No "page" key in response'
    assert 'per_page' in response_dict, 'No "per_page" key in response'


@pytest.mark.parametrize('params', TestData.params_list, ids=['by_city', 'by_dist', 'page',
                                                              'by_name', 'by_state', 'by_postal'])
def test_metadata_with_params(params):
    response = requests.get('https://api.openbrewerydb.org/breweries/meta', params=params)

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_dict = response.json()

    assert 'total' in response_dict, 'No "total" key in response'
    assert 'page' in response_dict, 'No "page" key in response'
    assert 'per_page' in response_dict, 'No "per_page" key in response'
