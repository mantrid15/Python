import os
import datetime
import pandas as pd
import constant as ct
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import pprint
# import testAvtomat as ta
import more_itertools as mi
from openpyxl import load_workbook


# def date_str_to_date(any_list, format_template):
#     # func форматирования исходного списка
#     nu_list = []
#     for i in any_list:
#         i = datetime.datetime.strptime(i, format_template).date()
#         nu_list.append(i)
#         nu_list.sort(reverse=True)
#     return nu_list
#
# def delete_extension(any_list):
#     # func форматирования исходного списка удаление расширения у файлов
#     nu_list = []
#     for i in any_list:
#         i = i[0:8:1]
#         # применён срез
#         nu_list.append(i)
#         nu_list.sort(reverse=True)
#     return nu_list

# func форматирования исходного списка
def date_str_to_date_and_delete_extension(any_list, format_template):
    nu_list = []
    for i in any_list:
        if len(i) > 8:
            i = i[0:8:1]
        i = datetime.datetime.strptime(i, format_template).date()
        nu_list.append(i)
        nu_list.sort(reverse=True)
    return nu_list


# возвращает полный список файлов с путями в папке АВТОМАТ
def list_files_source(a):
    path_to_files = []

    for i in a:
        path = i
        path_full = os.listdir(path)
        for j in path_full:
            substr = '~$'
            substr2 = 'newAvtomat'
            if substr not in j and substr2 in j:
                file_path = i + j

            path_to_files.append(file_path)
            path_to_files.sort()
            nu: set = set(path_to_files)
            # print(nu)
    return nu

# def list_files_source(a):
#     path_to_files = []
#     for i in a:
#         path = i
#         path_full = os.listdir(path)
#         for j in path_full:
#             files = i + j
#             path_to_files.append(files)
#     return path_to_files

#     возвращает массив с путями папкам с исходниками АВТОМАТАМИ
def path_to_dirs(a, b):
    path_array = []
    for i in a:
        path = b + i + "/"
        path_array.append(path)
    return path_array


# возвращает из кажждого файла в искомомой папки список листов требующих обработки
def xls_sheet(a, b):
    sheet_list = []
    for i in a:
        wb = pd.ExcelFile(i)
        # берётся файл
        names = wb.sheet_names
        # вынимается список листов
        result = list(set(b) & set(names))
        # сравнивается с эталонным списком
        result.sort()
        # сортируется
        sheet_list.append(result)
        # добавляется в общий массив
    return sheet_list


# принимает полный путь возвращает выборку по условию (свободно к продаже = 1)
# в процессе оставляет столбцы по списку, фильтрует по условию и оставляет строки по условию

def concat_list_2(a):
    project = ''
    # print("Выбрано по фильтру строк: " + str(len(a)))
    date = a.split(sep='/')[5]
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

        # if not nu_table_select.empty:
        # if len(nu_table_select) != 0:
        full_table.append(nu_table_select)

    nu_full_table = pd.concat(full_table)
    print('Список выжимки сделан по Проекту ' + project + ' Дата: - ' + date + " Выбрано по фильтру строк: " + str(len(nu_table_select)))
    return nu_full_table


# def concat_list_2(a):
#     project = ''
#     date = a.split(sep='/')[5]
#     str(date)
#     if a.find('DABL') > 0:
#         project = 'Дабл'
#     if a.find('MAYgorkiLns') > 0:
#         project = 'Май'
#     if a.find('MKV') > 0:
#         project = 'МК'
#     if a.find('NKkorenevo') > 0:
#         project = 'НК'
#     if a.find('NTM') > 0:
#         project = 'НТ'
#     if a.find('OB2') > 0:
#         project = 'ОБ2'
#     if a.find('TOP') > 0:
#         project = 'Тополя'
#     if a.find('VB2') > 0:
#         project = 'ВБ'
#     if a.find('YAR') > 0:
#         project = 'СЯ'
#
#     full_table = []
#     b = ""
#     if a.find('MAYgorkiLns') > 0:
#         b = ct.list_may
#     elif a.find('NKkorenevo') > 0:
#         b = ct.list_nk
#     else:
#         b = ct.list_all
#
#     for i in b:
#         my_table = pd.read_excel(io=a, engine='openpyxl', sheet_name=i)
#         nu_table_1 = my_table.loc[:, ct.headers_all]
#         nu_table_1['Проект'] = project
#         nu_table_1['Дата'] = date
#         nu_table_select = nu_table_1.loc[nu_table_1.loc[:, 'доступность к продаже'] == 1]
#
#         if not nu_table_select.empty:
#             full_table.append(nu_table_select)
#
#     nu_full_table = pd.concat(full_table)
#     return nu_full_table


# принимает список путей и имён файлов и в цикле применяет  concat_list_2
def full_book_excel_select(d):
    full_table = []
    print("Файлов в выборке: " + str(len(d)))
    for i in d:
        i = str(i)
        list1 = concat_list_2(i)
        full_table.append(list1)
        # print(full_table)
        # print(full_table)
    nu_full_table = pd.concat(full_table)
    print(len(nu_full_table))
    return nu_full_table
