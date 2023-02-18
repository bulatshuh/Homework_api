import pytest
import requests


def test_one_random_brewery():
    response = requests.get('https://api.openbrewerydb.org/breweries/random')

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_list_of_breweries = response.json()
    assert len(response_list_of_breweries) == 1, f'Wrong size of list in response,' \
                                                 f' 1 dict is expected'


number_of_breweries = [1, 5, 10, 15, 49]


@pytest.mark.parametrize('quantity', number_of_breweries)
def test_several_random_breweries(quantity):
    params = {
        'size': quantity
    }
    response = requests.get('https://api.openbrewerydb.org/breweries/random', params=params)

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_list_of_breweries = response.json()

    assert len(response_list_of_breweries) == quantity, f'Wrong size of list in response,' \
                                                        f' {quantity} is expected'


maximum_numbers = [50, 51]


@pytest.mark.parametrize('quantity', maximum_numbers)
def test_max_random_breweries(quantity):
    params = {
        'size': quantity
    }
    response = requests.get('https://api.openbrewerydb.org/breweries/random', params=params)

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_list_of_breweries = response.json()

    assert len(response_list_of_breweries) == 50, 'Wrong size of list in response, 50 is expected'
