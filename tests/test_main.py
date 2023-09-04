from utils.utils import file_func, line_date, from_to_key
import pytest


# фикстура для тестирования функции file_func() (в проекте есть тестовый  json)
@pytest.fixture
def json_fixture():
    file_path = '/Users/mac/Dev/Course_work_3/test.json'
    return file_path


# фикстура для тестирования функции получения времени line_date()
@pytest.fixture
def line_date_fixture():
    temp_data = [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]
    return temp_data


# фикстура для тестирования функции from_to_key()
@pytest.fixture
def from_to_key_fixture():
    temp_data = [{
        "from": "Visa Classic 6831982476737658",
        "to": "Счет 11111111111111111111"
    }]
    return temp_data


# вторая фикстура для тестирования функции from_to_key()
@pytest.fixture
def from_to_key_fixture_2():
    temp_data = [{
        "from": "Счет 11111111111111111111",
        "to": "Maestro 4598300720424501"
    }]
    return temp_data


def test_file_func(json_fixture):
    assert file_func(json_fixture, 'a') == [{'a': 10, 'b': 2, 'c': 3},
                                            {'a': 7, 'b': 8, 'c': 90},
                                            {'a': 4, 'b': 50, 'c': 6}]


def test_line_date(line_date_fixture):
    assert line_date(line_date_fixture, 0) == '26.08.2019'


def test_from_to_key(from_to_key_fixture, from_to_key_fixture_2):
    assert from_to_key(from_to_key_fixture, 'from', 0) == "Visa Classic 6831 98** **** 7658"
    assert from_to_key(from_to_key_fixture_2, 'from', 0) == "Счет **1111"
    assert from_to_key(from_to_key_fixture_2, 'to', 0) == "Maestro 4598 30** **** 4501"
