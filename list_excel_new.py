# файл для выгрузки из автоматов ИМ. Сначала создаётся файл по выборке из автоматов, после из него создаётся csv файл,
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

switcher = 0
# 1 - работа с демо базой, 0 - работа с основной базой
path_to_table = 'X:/аналитика/Отчеты/Автоматы по конкурентам/'
output_path = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
output_name = 'filter_free_sales.xlsx'
output_name_sheet = 'date'
name_xlsx_first = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/filter_free_sales_first.xlsx'
name_xlsx = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/filter_free_sales.xlsx'
name_csv = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/filter_free_sales.csv'
# print(path_to_table, output_path, output_name, output_name_sheet, sep='\n')
# путь к папке содержащей папки с АВТОМАТАМИ

# список папок в рабочей папке+
# dirs = list(map(os.listdir, path_to_table))
dirs = os.listdir(path_to_table)


#  полные пути с папками, лежащие в папке автоматы
def path_to_dirs(a):
    path_array = []
    for i in a:
        path = path_to_table + i + "/"
        path_array.append(path)
    return path_array

# full_path_to_dirs = list(map(path_to_dirs, dirs))
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

full_list_files = list_files_source(full_path_to_dirs)

print(full_list_files)


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
