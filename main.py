# делаем необходимые импорты
from utils.utils import (read_json, filter_by_status, sort_by_data,
                         data_transform, prepare_one_operation,
                         print_one_operation)

# объявляем константу с адресом json файла
FILENAME = '../Course_work_3/operations.json'

# открываем файл json и возвращаем список словарей
transactions = read_json(FILENAME)

# фильтруем наш список, оставляя только словари со значением 'state'='EXECUTED'
filter_transactions = filter_by_status(transactions)

# сортируем наш список по убыванию даты
sorted_date = sort_by_data(filter_transactions)

# переводим дату в заданный формат
transformed_data = data_transform(sorted_date)

# основной цикл программы
for i in range(5):
    result_dict = prepare_one_operation(transformed_data, i)
    print(print_one_operation(result_dict))
    print()
