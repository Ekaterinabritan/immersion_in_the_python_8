import os
import pickle
import csv
import json


# Задача 5
# Напишите функцию, которая ищет json файлы
# в указанной директории и сохраняет
# их содержимое в виде одноимённых pickle файлов.


def search_files(ext: str = '.json', dir_: str = '.') -> None:
    """
    Поиск файлов по расширению в текущей директории,
    Кодирование файлов байты и сохранение и в pickle.
    ext: расширение искомых файлов"""
    files = (file for file in os.listdir(dir_) if file.endswith(ext))

    for file in files:
        name, _ = os.path.splitext(file)
        with (open(file, 'r') as r_file,open(name + '.pickle', 'wb') as w_file):
            data = r_file.read()
            pickle.dump(file=w_file, obj=data)


# Задание №6
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.


def pickle_transformer(pickle_file_name) -> None:
    """
    Десериализует pickle файл в список словарей и записывает csv файл"""
    name, _ = os.path.splitext(pickle_file_name)
    with (
        open(pickle_file_name, 'rb') as file,
        open('task_6_restored_' + name + '.csv', 'w', encoding='utf-8') as w_file
    ):
        data = pickle.load(file)
        j_data = json.loads(data)
        field_names = j_data[0].keys()
        writer = csv.DictWriter(w_file, fieldnames=field_names, lineterminator='\n')
        writer.writeheader()
        for row in j_data:
            writer.writerow(row)


# Задание №7
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.


def reader_csv(csv_file_name: str) -> bytes:
    """Читает csv файл, отдает """
    with open(csv_file_name, 'r', encoding='utf-8') as f:
        reader = f.read()
        return pickle.dumps(reader)