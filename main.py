# делаем необходимые импорты
from utils.utils import file_func, from_to_key, line_date


# объявляем константу с адресом json файла
FILENAME = '../Course_work_3/operations.json'

# получаем список словарей из соответствующей функции
transactions = file_func(FILENAME)

# запускаем основной цикл программы, выводим результат
for i in range(5):
    if transactions[i]['state'] == "EXECUTED":
        print(line_date(transactions, i), end=' ')
        print(transactions[i]['description'])

        print(from_to_key(transactions, 'from', i), '--> ', end='')
        print(from_to_key(transactions, 'to', i))

        print(f"{transactions[i]['operationAmount']['amount']}", end=' ')
        print(f"{transactions[i]['operationAmount']['currency']['name']}")
        print()
