import json


def file_func(filename, sort_key='date') -> list:
    """"
    Открывает файл json, удаляет пустые словари, сортирует по ключу 'date'
    (по убыванию) и возвращает отсортированный список словарей
    """
    with open(filename, 'r', encoding='utf-8') as f:
        temp_data = json.load(f)

    no_sort_transactions = []

    for i in range(len(temp_data)):
        if temp_data[i] != {}:
            no_sort_transactions.append(temp_data[i])

    transactions = sorted(no_sort_transactions, key=lambda x: x[sort_key],
                          reverse=True)
    return transactions


def from_key_2(transactions: list, i: int) -> str:
    """
    Обрабатывает ключ 'from' и печатает результат
    количество элементов ключа 'from' равно 2 и не начинается со "Счет"
    """
    return f"{transactions[i]['from'].split(' ')[0]} " \
           f"{transactions[i]['from'].split(' ')[1][0:4]} " \
           f"{transactions[i]['from'].split(' ')[1][5:7]}** " \
           f"**** {transactions[i]['from'].split(' ')[1][-4:]} --> "


def from_key_2_c(transactions: list, i: int) -> str:
    """
    Обрабатывает ключ 'from' и печатает результат
    количество элементов ключа 'from' равно 2 и начинается со "Счет"
    """
    return f"{transactions[i]['from'].split(' ')[0]} " \
           f"**{transactions[i]['from'].split(' ')[1][-4:]} --> "


def from_key_3(transactions: list, i: int) -> str:
    """
    Обрабатывает ключ 'from' и печатает результат
    количество элементов ключа 'from' равно 3 и не начинается со "Счет"
    """
    return f"{transactions[i]['from'].split(' ')[0]} " \
           f"{transactions[i]['from'].split(' ')[1]} " \
           f"{transactions[i]['from'].split(' ')[2][0:4]} " \
           f"{transactions[i]['from'].split(' ')[2][5:7]}** " \
           f"**** {transactions[i]['from'].split(' ')[2][-4:]} --> "


def from_key_3_c(transactions: list, i: int) -> str:
    """
    Обрабатывает ключ 'from' и печатает результат
    количество элементов ключа 'from' равно 3 и он начинается со "Счет"
    """
    return f"{transactions[i]['from'].split(' ')[0]} " \
           f"**{transactions[i]['from'].split(' ')[2][-4:]} --> "


def to_key_2(transactions: list, i: int) -> str:
    """
    Обрабатывает ключ 'to' и печатает результат
    количество элементов ключа 'to' равно 2 и не начинается со "Счет"
    """
    return f"{transactions[i].get('to', '').split(' ')[0]} " \
           f"{transactions[i].get('to', '').split(' ')[1][0:4]} " \
           f"{transactions[i].get('to', '').split(' ')[1][5:7]}** " \
           f"**** {transactions[i].get('to', '').split(' ')[1][-4:]}"


def to_key_2_c(transactions: list, i: int) -> str:
    """
    Обрабатывает ключ 'to' и печатает результат
    количество элементов ключа 'to' равно 2 и начинается со "Счет"
    """
    return f"{transactions[i]['to'].split(' ')[0]} " \
           f"**{transactions[i]['to'].split(' ')[1][-4:]}"


def to_key_3(transactions: list, i: int) -> str:
    """
    Обрабатывает ключ 'to' и печатает результат
    количество элементов ключа 'to' равно 3 и не начинается со "Счет"
    """
    return f"{transactions[i].get('to', '').split(' ')[0]} " \
           f"{transactions[i].get('to', '').split(' ')[1]} " \
           f"{transactions[i].get('to', '').split(' ')[2][0:4]} " \
           f"{transactions[i].get('to', '').split(' ')[2][5:7]}** " \
           f"**** {transactions[i].get('to', '').split(' ')[2][-4:]} "


def to_key_3_c(transactions: list, i: int) -> str:
    """
    Обрабатывает ключ 'to' и печатает результат
    количество элементов ключа 'to' равно 3 и начинается со "Счет"
    """
    return f"{transactions[i].get('to', '').split(' ')[0]} " \
           f"**{transactions[i].get('to', '').split(' ')[2][-4:]}"
