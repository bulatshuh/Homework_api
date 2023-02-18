import requests
from datetime import date


def test_update_resource():
    data = {
        'id': '1',
        'title': f'test_{date.today()}',
        'body': f'test_{date.today()}',
        'userId': date.today(),
    }

    response = requests.put('https://jsonplaceholder.typicode.com/posts/1',
                            data=data
                            )

    assert response.status_code is 200, 'Wrong status code, 200 is expected'

    response_dict = response.json()

    assert response_dict['title'] == f'test_{date.today()}', 'Wrong "title" in response'
    assert response_dict['body'] == f'test_{date.today()}', 'Wrong "body" in response'
    assert response_dict['userId'] == f'{date.today()}', 'Wrong "user" id in response'
