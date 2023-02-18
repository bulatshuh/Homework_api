import requests


def test_search_breweries():
    params = {
        'query': 'cat',
        'per_page': '3'
    }
    response = requests.get('https://api.openbrewerydb.org/breweries/search', params=params)

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_list_of_breweries = response.json()

    for brewery in response_list_of_breweries:
        assert list(params.values())[0] in brewery['id'], f'Can\'t find {list(params.values())[0]} ' \
                                                          f'in "id" element in response'


def test_search_autocomplete():
    params = {
        'query': 'castle'
    }
    response = requests.get('https://api.openbrewerydb.org/breweries/autocomplete', params=params)

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_list = response.json()

    for brewery in response_list:
        assert list(params.values())[0] in brewery['id'], f'Can\'t find {list(params.values())[0]} ' \
                                                          f'in "id" element in response'

    assert len(response_list) <= 15, 'Maximum number of breweries returned in response (15) exceeds'
