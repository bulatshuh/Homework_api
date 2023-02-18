import requests


def test_single_brewery():
    response = requests.get('https://api.openbrewerydb.org/breweries/madtree-brewing-cincinnati')

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_dict = response.json()
    assert response_dict['id'] == 'madtree-brewing-cincinnati', 'Wrong id in response'
    assert response_dict['website_url'] == 'http://www.madtreebrewing.com', 'Wrong website_url ' \
                                                                            'in response'
