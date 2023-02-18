import requests


def test_random_sub_breed_one_image():
    response = requests.get('https://dog.ceo/api/breed/hound/afghan/images/random')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()
    assert 'hound-afghan' in response_dict['message'], f'Wrong breed in image link - ' \
                                                       f'{response_dict["message"]},' \
                                                       f' - expected: hound-afghan'


def test_random_sub_breed_multiple_image():
    response = requests.get('https://dog.ceo/api/breed/hound/blood/images/random/3')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()
    assert len(response_dict['message']) <= 3, 'Number of pictures in response more than requested'

    for picture in response_dict['message']:
        assert 'hound-blood' in picture, f'Wrong breed in image link - ' \
                                         f'{picture},' \
                                         f' - expected: hound-blood'


def test_random_sub_breed_all_image():
    response = requests.get('https://dog.ceo/api/breed/hound/ibizan/images')

    assert response.status_code is 200, 'Wrong status code! Expected: 200'

    response_dict = response.json()
    for picture in response_dict['message']:
        assert 'hound-ibizan' in picture, f'Wrong breed in image link - ' \
                                          f'{picture},' \
                                          f' - expected: hound-ibizan'
