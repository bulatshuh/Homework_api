import requests
import pytest
import random


def choose_random_breed():
    response_list_of_breeds = requests.get('https://dog.ceo/api/breeds/list/all')

    response_list_of_breeds_dict_json = response_list_of_breeds.json()

    response_list_of_breeds_dict = response_list_of_breeds_dict_json['message']

    response_list_of_breeds_list = []

    for key in response_list_of_breeds_dict.keys():
        element = key
        response_list_of_breeds_list.append(element)

    random_breed = random.choice(response_list_of_breeds_list)
    yield random_breed


@pytest.mark.parametrize('breed', choose_random_breed())
def test_random_breed_one_image(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()

    assert breed in response_dict['message'], f'Wrong breed in image link' \
                                              f' - {response_dict["message"]},' \
                                              f' - expected: {breed}'


@pytest.mark.parametrize('breed', choose_random_breed())
def test_random_breed_multiple_image(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random/3')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()
    assert len(response_dict['message']) <= 3, 'Number of pictures in response more than requested'

    for picture in response_dict['message']:
        assert breed in picture, f'Wrong breed in image link,' \
                                        f' - {picture}' \
                                        f' - expected: {breed}'


@pytest.mark.parametrize('breed', choose_random_breed())
def test_random_breed_all_image(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/images')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()
    print(response_dict)

    for picture in response_dict['message']:
        assert breed in picture, f'Wrong breed in image link,' \
                                        f' - {picture}' \
                                        f' - expected: {breed}'
