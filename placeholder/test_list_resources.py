import requests


def test_single_resource():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_dict = response.json()
    assert 'id' in response_dict, 'No "id" in dict in response'
    assert 'title' in response_dict, 'No "title" in dict in response'


def test_list_resources():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_list = response.json()

    for element in response_list:
        assert 'id' in element, 'No "id" in dict in response'
        assert 'title' in element, 'No "title" in dict in response'
