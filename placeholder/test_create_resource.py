import requests
from datetime import date


def test_create_resource():
    data = {
        'title': f'test_{date.today()}',
        'body': f'test_{date.today()}',
        'userId': date.today(),
    }

    response = requests.post('https://jsonplaceholder.typicode.com/posts',
                             data=data
                             )

    assert 200 <= response.status_code < 300, 'Wrong status code, 2** is expected'

    response_dict = response.json()

    assert response_dict['title'] == f'test_{date.today()}', 'Wrong "title" in response'
    assert response_dict['body'] == f'test_{date.today()}', 'Wrong "body" in response'
    assert response_dict['userId'] == f'{date.today()}', 'Wrong "user" id in response'
