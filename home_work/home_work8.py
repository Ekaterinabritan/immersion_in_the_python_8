import os
import sys
import csv
import json
import pickle
import pandas as pd

# функция для обхода:

def walkdir(dirname: str):
    for cur, _dirs, files in os.walk(dirname):
        pref = ''
        head, tail = os.path.split(cur)
        while head:
            pref += '-'
            head, _tail = os.path.split(head)
        print(pref+tail)
        for f in files:
            print(pref + '-' + f)

 #cохранение обхода в файл txt
def result_walkdir(filename: str = 'one_file_result.txt'):
    with open(filename, 'w') as sys.stdout:
        walkdir('.')

result_walkdir()

#Результаты обхода сохраните в json:
def txt_json(src_file: str = 'one_file_result.txt',
             out_file: str = 'one_result_js.json'):
    with open(src_file) as file, open(out_file, 'w') as json_file:
        items = []
        for line in file:
            if not line.strip():
                continue
            d = {}
            data = line.split('|')
            for val in data:
                key, sep, value = val.partition(':')
                d[key.strip()] = value.strip()
            items.append(d)
        json.dump(items, json_file)
    return items

#Результаты обхода сохраните в csv:

def json_csv(csv_file: str = 'one_file_csv.csv',
             out_file: str = 'one_result_js.json'):

    with open(out_file, encoding='utf-8') as inputfile:
        df = pd.read_json(inputfile)

    df.to_csv(csv_file, encoding='utf-8', index=False)


#Результаты обхода сохраните pickle:
def pkl_csv(csv_file: str = 'one_file_csv.csv',
             pkl_file: str = 'one_reslt_pkl.pkl'):
    with open(csv_file, 'r') as f:
        pickle.dump(list(csv.reader(f)), open(pkl_file, 'wb'))


def fun_result():
    txt_json()
    json_csv()
    pkl_csv()

fun_result()