# Задача 2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7). После каждого ввода добавляйте
# новую информацию в JSON файл. Пользователи
# группируются по уровню доступа. Идентификатор
# пользователя выступает ключём для имени. Убедитесь,
# что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные
# в файл данные должны сохраняться.

# Задача 3
# Напишите функцию, которая сохраняет созданный
# в прошлом задании файл в формате CSV.

import json


def add_usrs_json(filename: str = 'users.json'):
    """Добавление пользователей в json файл."""
    while True:
        try:
            with open(filename, 'r') as src:
                data = json.load(src)
        except FileNotFoundError:
            data = {str(i): [] for i in range(1, 8)}

        name = input('Ввведите имя: ')
        user_id = input('Введите ваш id: ')
        level = input('Введите ваш уровень доступа: ')
        data[level].append({'name': name, 'id': user_id})

        with open(filename, 'w') as res:
            json.dump(data, res, indent=4)


def json_to_csv(src_file: str = 'users.json',
                out_file: str = 'users.csv'):
    """Перевод из формата json в csv."""
    with open(src_file, 'r') as src:
        data = json.load(src)

    with open(out_file, 'w') as res:
        res.write('id,level,name')
        for level, users_lst in data.items():
            for user in users_lst:
                res.write(f'\n{user["id"]},{level},{user["name"]}')


# Задача 4
# Прочитайте созданный в прошлом задании csv файл
# без использования csv.DictReader. Дополните id до
# 10 цифр незначащими нулями. В именах первую букву
# сделайте прописной. Добавьте поле хеш на основе имени
# и идентификатора. Получившиеся записи сохраните в json
# файл, где каждая строка csv файла представлена как
# отдельный json словарь. Имя исходного и конечного
# файлов передавайте как аргументы функции.


def csv_to_json(src_file: str = 'users.csv',
                out_file: str = 'users_1.json',):
    """Перевод из csv к json формату."""
    with open(src_file, 'r') as src:
        data = list(map(lambda x: x.split(','),
                        src.read().split('\n')))

    for i in range(1, len(data)):
        data[i][0] = data[i][0].zfill(10)
        data[i][2] = data[i][2].capitalize()

        user_id = data[i][0]
        name = data[i][2]
        data[i].append(hash(user_id + name))

    data = data[1::]
    print(data)

    data = [{'id': u_id, 'level': level, 'name': uname, 'hash': uhash}
            for u_id, level, uname, uhash in data]

    with open(out_file, 'w') as res:
        json.dump(data, res, indent=4)