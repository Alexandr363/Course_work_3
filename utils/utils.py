import json

from datetime import date


def read_json(filename) -> list:
    """
    Открывает файл json и возвращает список словарей
    """
    with open(filename, 'r', encoding='utf-8') as f:
        transactions = json.load(f)
    return transactions


def filter_by_status(transactions) -> list:
    """
    Фильтрует список по ключу 'state', оставляя только равные 'EXECUTED'
    """
    sort_transactions = []
    for i in range(len(transactions)):
        if transactions[i].get('state') == 'EXECUTED':
            sort_transactions.append(transactions[i])
    return sort_transactions


def sort_by_data(transactions) -> list:
    """
    Сортируем список по убыванию даты
    """
    sort_transactions = sorted(transactions, key=lambda x: x['date'],
                               reverse=True)
    return sort_transactions


def data_transform(transactions: list) -> list:
    """
    Приводит поле 'date' к заданному формату
    """
    for i in range(len(transactions)):
        a = transactions[i]['date'].split('T')[0]
        b = a.split('-')
        result = [int(b[0]), int(b[1]), int(b[2])]
        the_date = date(result[0], result[1], result[2])
        format_date = the_date.strftime("%d.%m.%Y")
        transactions[i]['date'] = format_date
    return transactions


def mask_card(card_number: str) -> str:
    """
    Обрабатывает название карты/счёта
    """
    if card_number == '':
        return ''
    *card, number = card_number.split()
    return ' '.join(card)


def mask_number(card_number: str) -> str:
    """
    Обрабатывает номер карты/счёта
    """
    if card_number == '':
        return ''
    number = card_number.split()[-1]
    if len(number) == 16:
        return f"{number[0:4]} {number[4:6]}** **** {number[-4:]}"
    elif len(number) == 20:
        return f"**{number[-4:]}"


def prepare_one_operation(transactions: list, i: int) -> dict:
    """
    Подготавливает данные для вывода информации по 1 операции
    """
    result = {
              '1': (transactions[i]['date'], transactions[i]['description']),
              '2': (mask_card(transactions[i].get('from', '')),
                    mask_number(transactions[i].get('from', '')),
                    mask_card(transactions[i]['to']),
                    mask_number(transactions[i]['to'])),
              '3': (transactions[i]['operationAmount']['amount'],
                    transactions[i]['operationAmount']['currency']['name'])
              }
    return result


def print_one_operation(result_dict: dict) -> str:
    """
    Вывод информации по 1 операции в запрошенном виде
    """
    return f"{result_dict['1'][0]} {result_dict['1'][1]} \n" \
           f"{result_dict['2'][0]} {result_dict['2'][1]}" \
           f" --> {result_dict['2'][2]} {result_dict['2'][3]} \n" \
           f"{result_dict['3'][0]} {result_dict['3'][1]}"
