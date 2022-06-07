import pytest
import requests

from utils.read_csv_file_util import read_csv_file
from definitions import ZIP_CODE_TEST_DATA_FILE_PATH


@pytest.mark.parametrize('country_code, zip_code, expected_location', read_csv_file(ZIP_CODE_TEST_DATA_FILE_PATH))
def test_using_test_data_object_get_location_data_check_place_name(country_code, zip_code, expected_location):
    response = requests.get(f'http://api.zippopotam.us/{country_code}/{zip_code}')
    response_body = response.json()
    assert response_body['places'][0]['place name'] == expected_location, f'Location is not {expected_location}'


def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert response.status_code == 200, 'Response status code is not 200'


def test_get_locations_for_us_90210_check_content_type_equals_json():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert response.headers['Content-Type'] == 'application/json', 'Response Content-Type is not JSON'


def test_get_locations_for_us_90210_check_country_equals_united_states():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert response_body['country'] == 'United States', 'Country is not USA'


def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert response_body['places'][0]['place name'] == 'Beverly Hills', 'City is not Beverly Hills'


def test_get_locations_for_us_90210_check_one_place_is_returned():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert len(response_body['places']) == 1, 'Response length is not 1'
