import json

# атрибуты dump и dumps
my_dict = {
    "id": 123,
    "name": "Clementine Bauche",
    "username": "Cleba",
    "email": "cleba@corp.mail.ru",
    "address": {
        "street": "Central",
        "city": "Metropolis",
        "zipcode": "123456"
    },
    "phone": "+7-999-123-45-67"
}
res = json.dumps(my_dict, indent=2, # форматирование с отступами
                 separators=(',', ':'), # принимает кортеж, где:
                                        # 1-ый символ - разделитель элементов
                                        # 2-ой символ - разделитель ключа и значения
                # символы лучше не менять, т.к. это json. Можно регулировать только пробелы для экономии
                 sort_keys=True) # сортировка ключей по алфавиту
print(res)
