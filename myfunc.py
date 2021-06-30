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


# func форматирования исходного списка
# def date_str_to_date(any_list, format_template):
#     nu_list = []
#     for i in any_list:
#         i = datetime.datetime.strptime(i, format_template).date()
#         nu_list.append(i)
#         nu_list.sort(reverse=True)
#     return nu_list

# func форматирования исходного списка удаление расширения у файлов
# def delete_extension(any_list):#
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
            substr3 = 'VBdom'
            if substr not in j and substr2 in j and substr3 not in j:
                file_path = i + j
            path_to_files.append(file_path)
            path_to_files.sort()
            nu: set = set(path_to_files)
            # print(nu)
        return nu


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


# принимает массив и выгружает его в эксельный файл
def print_to_excel(a, b, c, d):
    # a - обрабатываемая таблица, список полных путей с именами файлов 'X:/аналитика/Отчеты/Автоматы по конкурентам/14.04.21/newAvtomatYAR.xlsx'
    # b - путь к папке вывода, место где будет расположен итоговый файл эксель
    # c - нименование выходного файла
    # d - имя листа в создаваемом файле
    # create excel writer object
    doc_to_excel = pd.ExcelWriter(b + c, engine='xlsxwriter')
    # write dataframe to excel
    a.to_excel(doc_to_excel, d, index=False)
    # save the excel
    doc_to_excel.save()
    print('DataFrame is written successfully to Excel File.')


# принимает добавленный массив (новые данные), объединяет со старыми данными, создаеёт обновлённый массив и
# перезаписывает его поверх старых данных в эксельный файл
def add_print_to_excel(a, b):
    # b - обрабатываемая таблица, список полных путей с именами файлов 'X:/аналитика/Отчеты/Автоматы по конкурентам/14.04.21/newAvtomatYAR.xlsx'
    # a - путь к папке вывода, место где будет расположен итоговый файл эксель
    if b is None:
        return print("Состояние обновлено. Источник и выходной файл выравнены. Операция остановлена.")
    # create excel writer object
    df = pd.read_excel(io=a, engine='openpyxl', sheet_name='date')
    old_table = df.loc[:]
    nu_table = b
    full_table = pd.concat([old_table, nu_table])
    doc_to_excel = pd.ExcelWriter(a, engine='xlsxwriter')
    # write dataframe to excel
    full_table.to_excel(doc_to_excel, sheet_name='date', index=False)
    # save the excel
    doc_to_excel.save()

    print('DataFrame is written successfully to Excel File.')
