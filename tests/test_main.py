from utils.data_func import file_func
from utils.data_func import from_key_2, from_key_2_c
from utils.data_func import from_key_3, from_key_3_c
from utils.data_func import to_key_2, to_key_2_c
from utils.data_func import to_key_3, to_key_3_c
import pytest


@pytest.fixture
def json_fixture():
    temp_data = '/Users/mac/Dev/Course_work_3/test.json'
    return temp_data


@pytest.fixture
def key_fixture_2():
    temp_data = [{
        "from": "Card 2222222222222222",
        "to": "To 11111111111111111111"
    }]
    return temp_data


@pytest.fixture
def key_fixture_2_c():
    temp_data = [{
        "from": "Счет 22222222222222222222",
        "to": "Счет 11111111111111111111"
    }]
    return temp_data


@pytest.fixture
def key_fixture_3():
    temp_data = [{
        "from": "Test Card 3333333333333333",
        "to": "My Card 55555555555555555555"
    }]
    return temp_data


@pytest.fixture
def key_fixture_3_c():
    temp_data = [{
        "from": "Счет Card 3333333333333333",
        "to": "Счет Test 55555555555555555555"
    }]
    return temp_data


def test_file_func(json_fixture):
    assert file_func(json_fixture, 'a') == [{'a': 444, 'b': 555, 'c': 666},
                                            {'a': 111, 'b': 222, 'c': 333}]


def test_from_key_2(key_fixture_2):
    assert from_key_2(key_fixture_2, 0) == 'Card 2222 22** **** 2222 --> '


def test_from_key_2_c(key_fixture_2_c):
    assert from_key_2_c(key_fixture_2_c, 0) == 'Счет **2222 --> '


def test_from_key_3(key_fixture_3):
    assert from_key_3(key_fixture_3, 0) == 'Test Card 3333 33** **** 3333 --> '


def test_from_key_3_c(key_fixture_3_c):
    assert from_key_3_c(key_fixture_3_c, 0) == 'Счет **3333 --> '


def test_to_key_2(key_fixture_2):
    assert to_key_2(key_fixture_2, 0) == 'To 1111 11** **** 1111'


def test_to_key_2_c(key_fixture_2_c):
    assert to_key_2_c(key_fixture_2_c, 0) == 'Счет **1111'


def test_to_key_3(key_fixture_3):
    assert to_key_3(key_fixture_3, 0) == 'My Card 5555 55** **** 5555 '


def test_to_key_3_c(key_fixture_3_c):
    assert to_key_3_c(key_fixture_3_c, 0) == 'Счет **5555'
