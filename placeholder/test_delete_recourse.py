import requests


def test_delete_resource():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_text = response.json()
    assert response_text == {}, 'Response is not empty, but should be'
