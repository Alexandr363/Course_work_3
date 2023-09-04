import json

from datetime import date


def file_func(filename, sort_key: str = 'date') -> list:
    """"
    Открывает файл json, удаляет пустые словари, сортирует по заданному ключу
    (по убыванию) и возвращает отсортированный список словарей
    """
    no_sort_transactions = []

    with open(filename, 'r', encoding='utf-8') as f:
        temp_data = json.load(f)

    for i in range(len(temp_data)):
        if temp_data[i] != {}:
            no_sort_transactions.append(temp_data[i])

    transactions = sorted(no_sort_transactions, key=lambda x: x[sort_key],
                          reverse=True)
    return transactions


def from_to_key(transactions: list, key: str, i: int) -> str:
    if len(transactions[i].get(key, ' ').split(' ')) == 3:
        return f"{transactions[i].get(key, ' ').split(' ')[0]} " \
               f"{transactions[i].get(key, ' ').split(' ')[1]} " \
               f"{transactions[i].get(key, ' ').split(' ')[2][:4]} " \
               f"{transactions[i].get(key, ' ').split(' ')[2][4:6]}** " \
               f"**** {transactions[i].get(key, ' ').split(' ')[2][-4:]}"
    elif len(transactions[i].get(key, ' ').split(' ')) == 2:
        if transactions[i].get(key, ' ').split(' ')[0] == 'Счет':
            return f"{transactions[i].get(key, ' ').split(' ')[0]} " \
                   f"**{transactions[i].get(key, ' ').split(' ')[1][-4:]}"
        else:
            return f"{transactions[i].get(key, ' ').split(' ')[0]} " \
                   f"{transactions[i].get(key, ' ').split(' ')[1][:4]} " \
                   f"{transactions[i].get(key, ' ').split(' ')[1][4:6]}** " \
                   f"**** {transactions[i].get(key, ' ').split(' ')[1][-4:]}"


def line_date(transactions: list, i: int) -> str:
    """
    Выбирает ключ 'date', форматирует его и возвращает дату
    """
    a = transactions[i]['date'].split('T')
    b = a[0]
    c = b.split('-')
    result = [int(num) for num in c]
    the_date = date(result[0], result[1], result[2])
    return the_date.strftime("%d.%m.%Y")
