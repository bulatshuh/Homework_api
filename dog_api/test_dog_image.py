import requests
import pytest
import random


def test_one_random_image():
    response = requests.get('https://dog.ceo/api/breeds/image/random')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()

    assert response_dict['status'] == 'success', 'Wrong json status!'
    assert 'message' in response_dict, 'No message in json1'
    assert '.jpg' in response_dict['message'], 'Image is not in jpg format!'


@pytest.mark.parametrize('number', [0, 5, 15, 25, 35, 45])
def test_multiple_random_image(number):
    response = requests.get(f'https://dog.ceo/api/breeds/image/random/{number}')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()

    if number == 0:
        assert len(response_dict['message']) is 1, f'Wrong number of images,' \
                                                    f'expected 1 empty element'
    else:
        assert len(response_dict['message']) is number, f'Wrong number of images,' \
                                                   f'expected {number}'


def test_maximum_random_image():
    response = requests.get(f'https://dog.ceo/api/breeds/image/random/50')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()

    assert len(response_dict['message']) is 50, 'Maximum images number exceeds, expected 50'


def test_more_maximum_random_image():
    # choose random number for pictures from 51 to 150 (more than maximum)
    random_number = random.randint(51, 150)

    response = requests.get(f'https://dog.ceo/api/breeds/image/random/{random_number}')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()

    assert len(response_dict['message']) is 50, 'Maximum images number exceeds, expected 50'
