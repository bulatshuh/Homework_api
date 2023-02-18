import requests


def test_breed_list():
    response = requests.get('https://dog.ceo/api/breeds/list/all')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()

    assert response_dict['status'] == 'success', 'Wrong json status!'
    assert 'message' in response_dict, 'No message in json'
