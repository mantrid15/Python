import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import os
import datetime
import pprint
import myfunc as mf
import more_itertools as mi
from openpyxl import load_workbook

final_dir = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
# финальное размещение выходных файлов

# исходное местоположение отчётов/автоматов от И.М,
path_to_table = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/12_sourceProjectAvtomat/'
# путь к папке содержащей папки с АВТОМАТАМИ
dirs = os.listdir(path_to_table)
# список папок в рабочей папке

full_path_to_dirs = mf.path_to_dirs(dirs, path_to_table)
#  список путей к файлам
full_list_files = mf.list_files_source(full_path_to_dirs)
# список файлов в папке АВТОМАТОВ
# print(*full_list_files, sep='\n')

path = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/12_sourceProjectAvtomat/26.05.21/newAvtomatMAYgorkiLns.xlsx'
# wb = load_workbook(path)
xls = pd.read_excel(path, sheet_name=None)
# print(xls.keys())
# print(wb)
list_all = ['1', '2', '3', '4', '5',
            '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20',
            '21']
list_may = ['1', '2', '3', '4', '5',
            '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20',
            '21']
list_nk = ['1', '2', '3', '4', '5', '6']

headers_all = ['комнат',
               'площадь',
               'доступность к продаже',
               'стоимость',
               'ID квартиры',
               'Стоимость со скидкой']

headers_may = []
headers_nk = []
# список листов в искомых файлах, содержащих требуемые данные

# print(*mf.xls_sheet(full_list_files, list_for_download), sep='\n')

list_temp = full_list_files[1]

list_temp_all = full_list_files[2]

y_table = pd.read_excel(io=list_temp_all, engine='openpyxl')
print(y_table.columns)


print(list_temp)
# print(*mf.xls_sheet(list_temp, list_for_download))


def concat_list(b):
    full_table = []

    for i in b:
        my_table = pd.read_excel(io=list_temp, engine='openpyxl', sheet_name=i)
        # print(my_table.columns)
        nu_table_1 = my_table.loc[:, ['комнат', 'площадь',
                                    'доступность к продаже',
                                    'стоимость',
                                    'ID квартиры',
                                    'Стоимость со скидкой']]
        nu_table_select = nu_table_1.loc[nu_table_1.loc[:, 'доступность к продаже'] == 1]
        if nu_table_select.empty == False:
            full_table.append(nu_table_select)
    nu_full_table = pd.concat(full_table)
    return nu_full_table
# принимает полный путь с именем файла и возвращает конкатенированнй список если в файле более 1го листа для рассчёта

# print(concat_list(list_may))

def concat_list_2(a):
    full_table = []
    b = ""
    if a.find('MAYgorkiLns') > 0:
        b = list_may
    elif a.find('NKkorenevo') > 0:
        b = list_nk
    else:
        b = list_all

    for i in b:
        my_table = pd.read_excel(io=a, engine='openpyxl', sheet_name=i)
        # print(my_table.columns)
        nu_table_1 = my_table.loc[:, headers_all]
        nu_table_select = nu_table_1.loc[nu_table_1.loc[:, 'доступность к продаже'] == 1]
        if not nu_table_select.empty:
            full_table.append(nu_table_select)

    nu_full_table = pd.concat(full_table)
    return nu_full_table


# print(concat_list_2(list_temp))



# print(nu_table.tail(10))
# print(my_table)

# my_table = pd.read_excel(io=a, engine='openpyxl', sheet_name=i)
# # print(my_table.columns)
# nu_table = my_table.loc[:, ['комнат', 'площадь',
#                             'доступность к продаже',
#                             'стоимость',
#                             'ID квартиры',
#                             'Стоимость со скидкой']]
# nu_table_select = nu_table.loc[nu_table.loc[:, 'доступность к продаже'] == 1]
# print(nu_table)
