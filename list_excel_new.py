# файл для выгрузки из автоматов ИМ.
# Сначала создаётся файл по выборке из автоматов, после из него создаётся csv файл,

# после при обновлении добавляется недостающее


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import os

from openpyxl import load_workbook
import constant as ct
from io import StringIO
import prettytable as pt

# модули регулирующие параметры предстваления вывода при debug
pd.set_option('display.max_rows', 1000000)
pd.set_option('display.max_columns', 1000000)
pd.set_option('display.width', 1000000)
pd.options.display.float_format = '{:.2f}'.format

path_to_table = 'X:/аналитика/Отчеты/Автоматы по конкурентам/'
output_path = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
output_name = 'filter_free_sales.xlsx'
output_name_sheet = 'date'

name_xlsx = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/filter_free_sales.xlsx'
name_csv = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/filter_free_sales.csv'
# print(path_to_table, output_path, output_name, output_name_sheet, sep='\n')
# путь к папке содержащей папки с АВТОМАТАМИ

# список папок в рабочей папке+
dirs = os.listdir(path_to_table)


#  полные пути с папками, лежащие в папке автоматы
def path_to_dirs(a):
    path_array = []
    for i in a:
        path = path_to_table + i + "/"
        path_array.append(path)
    return path_array


full_path_to_dirs = path_to_dirs(dirs)


# print(full_path_to_dirs)


#  список путей к файлам
def list_files_source(a):
    path_to_files = []
    for i in a:
        path = i
        path_full = os.listdir(path)
        for j in path_full:
            substr = '~$'
            substr2 = 'newAvtomat'
            substr3 = 'VBdom'
            if substr not in j and substr2 in j and substr3 not in j:
                file_path = i + j
            path_to_files.append(file_path)
            path_to_files.sort()
            nu: set = set(path_to_files)
            # print(nu)
    return nu


# полный список путей с именами файлов
full_list_files = list_files_source(full_path_to_dirs[0:2])


# print(full_list_files)


def concat_list(a):
    counter = 0
    project = ''
    if a.find('Автоматы') > 0:
        ind = 4
    else:
        ind = 5
    date = a.split(sep='/')[ind]
    str(date)
    if a.find('DABL') > 0:
        project = 'Дабл'
    if a.find('MAYgorkiLns') > 0:
        project = 'Май'
    if a.find('MKV') > 0:
        project = 'МК'
    if a.find('NKkorenevo') > 0:
        project = 'НК'
    if a.find('NTM') > 0:
        project = 'НТ'
    if a.find('OB2') > 0:
        project = 'ОБ2'
    if a.find('TOP') > 0:
        project = 'Тополя'
    if a.find('VB2') > 0:
        project = 'ВБ'
    if a.find('YAR') > 0:
        project = 'СЯ'
    b = ""
    if a.find('MAYgorkiLns') > 0:
        b = ct.list_may
    elif a.find('NKkorenevo') > 0:
        b = ct.list_nk
    else:
        b = ct.list_all
    full_table = []

    for i in b:
        my_table = pd.read_excel(io=a, engine='openpyxl', sheet_name=i)
        nu_table_1 = my_table.loc[:, ct.headers_all]
        nu_table_1['Проект'] = project
        nu_table_1['Дата'] = date
        nu_table_select = nu_table_1.loc[nu_table_1.loc[:, 'доступность к продаже'] == 1]

        if len(nu_table_select) == 0:
            nu_table_select = pd.DataFrame(data=None, columns=ct.headers_all)
        full_table.append(nu_table_select)

    nu_full_table = pd.concat(full_table)
    print(f'Список по Проекту {project} - Дата: - {date}  Выбрано по фильтру строк: ' + str(len(nu_table_select)))
    return nu_full_table


# принимает список путей/имён файлов, применяет функ concat_list return


def full_book_excel_select(d):
    if d is None:
        return print("Состояние обновлено. Источник и выходной файл выравнены")
    full_table = []
    counter = len(d)
    print(f"Файлов в выборке: {counter}")
    for i in d:
        i = str(i)
        list1 = concat_list(i)
        full_table.append(list1)
        counter = counter - 1
        if counter > 0:
            print(f"Осталось в выборке: {counter}")
        else:
            print('Выгрузка закончена')

    nu_full_table = pd.concat(full_table)

    return nu_full_table


table_list_full = full_book_excel_select(full_list_files)
print(table_list_full)


#  чтение файла со старыми даннными
# old_list_xlsx = pd.read_excel(name_xlsx, engine='openpyxl', sheet_name='date')

# получение списка уникальных дат
# old_list_date = set(old_list_xlsx.loc[:, 'Дата'])

# получение разницы между старыми данными и новыми выгрузками
# dif_list_date = list(set(dirs) - set(old_list_date))

# возвращает полный список новых файлов с путями в папке АВТОМАТ
# dif_table_path = mf.list_files_source(mf.path_to_dirs(dif_list_date, path_to_table))
# print(type(dif_table_path))
# создаеёт новый dataFrame для добавления к существующей базе
# dif_table = mf.full_book_excel_select(dif_table_path)
# print(dif_table)
# выгрузка в имеющийся файл, с перезаписью поверх старых данных
# mf.add_print_to_excel(name_xlsx, dif_table)

# ОБРАБОТКА ВЫГРУЖЕНЫХ ИЗ АВТОМАТОВ И.М. ДАННЫХ С ИСПОЛЬЗОВАНИЕМ SCV ФАЙЛОВ
#
# old_list_csv = pd.read_csv(name_csv)
# print(old_list_csv)

# old_list_date_csv = set(old_list_csv.loc[:, 'Дата'])


def print_to_csv(a):
    # b - обрабатываемая таблица, список полных путей с именами файлов 'X:/аналитика/Отчеты/Автоматы по конкурентам/14.04.21/newAvtomatYAR.xlsx'
    # a - путь к папке вывода, место где будет расположен итоговый файл эксель
    # create excel writer object
    df = pd.read_excel(io=a, engine='openpyxl', sheet_name='date')
    table = df.loc[:]
    table.to_csv(name_csv, sep='|', encoding='cp1251')
    print('Добавление данных в CSV-файл завершено.')

# print_to_csv(name_xlsx)
