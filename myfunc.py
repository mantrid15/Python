import os
import datetime
import pandas as pd
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

def date_str_to_date_and_delete_extension(any_list, format_template):
    # func форматирования исходного списка
    nu_list = []
    for i in any_list:
        if len(i) > 8:
            i = i[0:8:1]
        i = datetime.datetime.strptime(i, format_template).date()
        nu_list.append(i)
        nu_list.sort(reverse=True)
    return nu_list

def list_files_source(a):
    path_to_files = []
    for i in a:
        path = i
        path_full = os.listdir(path)
        for j in path_full:
            files = i +j
            path_to_files.append(files)
    return path_to_files
# возвращает полный список файлов с путями в папке АВТОМАТ

def path_to_dirs(a,b):
    path_array = []
    for i in a:
        path = b + i + "/"
        path_array.append(path)
    return path_array
#     возвращает массив с путями папкам с исходниками АВТОМАТАМИ

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
# возвращает из кажждого файла в искомомой папки список листов требующих обработки