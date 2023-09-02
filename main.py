# импортируем необходимые функции
from utils.data_func import file_func
from utils.data_func import from_key_2, from_key_2_c
from utils.data_func import from_key_3, from_key_3_c
from utils.data_func import to_key_2, to_key_2_c
from utils.data_func import to_key_3, to_key_3_c


# объявляем константу с адресом json файла
FILENAME = '../Course_work_3/operations.json'

# получаем список словарей из соответствующей функции
transactions = file_func(FILENAME)

# запускаем основной цикл программы, получаем необходимое количество операций
for i in range(6):
    # берём только операции с ключом state = 'EXECUTED'
    if transactions[i]['state'] == 'EXECUTED':
        # переформатируем и выводим 1 строку <дата перевода>
        print(f"{transactions[i]['date'][8:10]}."
              f"{transactions[i]['date'][5:7]}."
              f"{transactions[i]['date'][0:4]}", end=' ')

        # выводим 2 часть 1 строки <описание перевода>
        print(transactions[i]['description'])

        # выводим 1 часть 2 строки <откуда> <from>
        if len((transactions[i].get('from', '').split(' '))) == 2:
            if (transactions[i].get('from', '').split(' ')[0]) == 'Счет':
                print(from_key_2_c(transactions, i), end=' ')
            elif (transactions[i].get('from', '').split(' ')[0]) != 'Счет':
                print(from_key_2(transactions, i), end=' ')

        elif len((transactions[i].get('from', '').split(' '))) == 3:
            if (transactions[i].get('from', '').split(' ')[0]) == 'Счет':
                print(from_key_3_c(transactions, i), end=' ')
            elif (transactions[i].get('from', '').split(' ')[0]) != 'Счет':
                print(from_key_3(transactions, i), end=' ')

        # выводим 2 часть 2 строки <куда> <to>
        if len((transactions[i].get('to', '').split(' '))) == 2:
            if (transactions[i].get('to', '').split(' ')[0]) == 'Счет':
                print(to_key_2_c(transactions, i))
            elif (transactions[i].get('to', '').split(' ')[0]) != 'Счет':
                print(to_key_2(transactions, i))

        if len((transactions[i].get('to', '').split(' '))) == 3:
            if (transactions[i].get('to', '').split(' ')[0]) == 'Счет':
                print(to_key_3_c(transactions, i))
            elif (transactions[i].get('to', '').split(' ')[0]) != 'Счет':
                print(to_key_3(transactions, i))

    # выводим 3 строку <сумма перевода> <валюта>
        print(f"{transactions[i]['operationAmount']['amount']}"
              f" {transactions[i]['operationAmount']['currency']['name']}")
    print()
