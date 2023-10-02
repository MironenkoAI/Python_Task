import json

with open('user.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f) 
    # преобразует json-файл в dict или list (Python)

print(f'{type(json_file) = }\n{json_file = }')
print(f'{json_file["name"] = }')
print(f'{json_file["address"]["geo"] = }')
print(f'{json_file["email"] = }')


with open('new_user.json', 'r', encoding='utf-8') as f:
    new_dict = json.load(f)
print(f'{new_dict = }')