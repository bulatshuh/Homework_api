import requests
import pytest
from test_data import TestData


@pytest.mark.parametrize('params', TestData.params_list, ids=['by_city', 'by_dist', 'page',
                                                              'by_name', 'by_state', 'by_postal'])
def test_list_breweries_with_params(params):
    response = requests.get('https://api.openbrewerydb.org/breweries', params=params)

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_list_of_breweries = response.json()

    for brewery in response_list_of_breweries:
        assert 'id' in brewery, 'No "id" element in response'
        assert brewery['id'] is not None, '"id" element is Null'
