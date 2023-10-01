import json

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование",
    "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}

dict_to_json_text = json.dumps(my_dict)
    # преобразует dict или list (Python) в json-строку
    # некоторые символы и рус.яз. будут закодированы, но верны при обратном преобразовании
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)
# или использовать дополнительно ensure_ascii, чтобы отображался русский
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')