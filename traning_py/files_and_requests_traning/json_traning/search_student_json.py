import json

with open('students.json', 'r') as file_json:
    data = json.load(file_json)


def search_json(file, key='Name', value='Yui'):
    # Фильтруем и ищем по нужным нам даннмы key value
    # Результат объекты в списке
    result = list(filter(lambda obj: value in obj[key], file))
    return result


print(search_json(data))
