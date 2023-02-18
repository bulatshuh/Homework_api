import requests
import pytest

breed_list = ['shihtzu', 'spaniel', 'spitz', 'springer',
              'stbernard', 'terrier', 'tervuren', 'vizsla', 'waterdog', 'weimaraner', 'whippet',
              'wolfhound']


@pytest.mark.parametrize('breed', breed_list)
def test_browse_breed_random_image(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()

    assert response_dict['status'] == 'success', 'Wrong json status!'
    assert breed in response_dict['message'], f'No {breed} in picture link -' \
                                              f' {response_dict["message"]}'
    assert '.jpg' in response_dict['message'], 'Image is not in jpg format!'
