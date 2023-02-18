import requests
from datetime import date


def test_patch_resource():
    data = {
        'title': f'test_{date.today()}',
    }

    response = requests.patch('https://jsonplaceholder.typicode.com/posts/1',
                              data=data
                              )

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_dict = response.json()

    assert response_dict['title'] == f'test_{date.today()}', 'Wrong "title" in response'
    assert 'id' in response_dict, 'No "id" in response'
    assert 'body' in response_dict, 'No "body" in response'
    assert 'userId' in response_dict, 'No "user id" in response'
