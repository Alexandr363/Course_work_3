import pytest

from utils.utils import (filter_by_status, sort_by_data, data_transform,
                         mask_card, mask_number, prepare_one_operation)


@pytest.fixture
def filter_by_status_fixture():
    data = [{"state": "CANCELED"}, {"state": "CANCELED"}, ]
    return data


@pytest.fixture
def sort_by_data_fixture():
    data = [{"date": "2018-08-26T10:50:58.294041"},
            {"date": "2019-08-26T10:50:58.294041"}, ]
    return data


@pytest.fixture
def mask_card_fixture():
    data = "Visa Classic 4610247282706784"
    return data


@pytest.fixture
def mask_number_fixture():
    data = "Visa Classic 4610247282706784"
    return data


@pytest.fixture()
def prepare_one_operation_fixture():
    data = {
        "id": 431131847,
        "state": "EXECUTED",
        "date": "05.05.2018",
        "operationAmount": {
            "amount": "56071.02",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "MasterCard 9454780748494532",
        "to": "Счет 51958934737718181351"
    },
    return data


def test_filter_by_status(filter_by_status_fixture):
    assert filter_by_status(filter_by_status_fixture) == []


def test_sort_by_data(sort_by_data_fixture):
    assert sort_by_data(sort_by_data_fixture) == [
        {"date": "2019-08-26T10:50:58.294041"},
        {"date": "2018-08-26T10:50:58.294041"}, ]


def test_data_transform(sort_by_data_fixture):
    assert data_transform(sort_by_data_fixture) == [
        {"date": "26.08.2018"},
        {"date": "26.08.2019"}, ]


def test_mask_card(mask_card_fixture):
    assert mask_card(mask_card_fixture) == 'Visa Classic'


def test_mask_number(mask_number_fixture):
    assert mask_number(mask_number_fixture) == '4610 24** **** 6784'


def test_prepare_one_operation(prepare_one_operation_fixture):
    assert prepare_one_operation(prepare_one_operation_fixture, 0) == {
        '1': ('05.05.2018', 'Перевод с карты на счет'),
        '2': ('MasterCard', '9454 78** **** 4532', 'Счет', '**1351'),
        '3': ('56071.02', 'руб.')}
