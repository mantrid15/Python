import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import os
import pprint
import testAvtomat as ta
import more_itertools as mi

# from nltk import flatten

from openpyxl import load_workbook

path_to_table = ta.selection_dir
# print(path_to_table)
# print(path_to_table)

# table_date = '310820'
# table_name = '/'+'newAvtomatNTM'
# table_ext = '.xlsx'
# full_name = path_to_table+table_date+table_name+table_ext

dirs = os.listdir(path_to_table)
# список папок в рабочей папке
# print(dirs)
def path_to_dirs(a):
    path_array = []
    for i in a:
        path = path_to_table + i + "/"
        path_array.append(path)
    return path_array
#     возвращает массив с путями папкам с исходниками АВТОМАТАМИ

full_path_to_dirs = path_to_dirs(dirs)
# print(full_path_to_dirs)


def list_files_source(a):
    path_to_files = []
    for i in a:
        path = i
        path_full = os.listdir(path)
        for j in path_full:
            files = i +j
            path_to_files.append(files)

    return path_to_files
# возвращает польный список файлов с путями в папке АВТОМАТ


full_list_files = list_files_source(full_path_to_dirs)
print(full_list_files)

       #  print(path_array_2)
       #
       #  print(dirs_contains)
       #  full_path = []
       #  path_array = path_array + path
       #  print(path_array)
       # список путей к искомым файлам
       #      for j in dirs_contains:
       #      j = path + j
       #      # j = path_to_table + i + j
       #      path_array.append(j)
       #      # path_array.append(i)
       #      full_path.append(path_array)
       #  print(full_path)
       #  print(path_array)
       #  path_array = path_array + path
       #  list(mi.flatten(path_array))
# def sub_dirs_files(path, direct):
# print(dirs)
# wb = load_workbook(full_name)
# print(wb.worksheets)

# os.chdir(ta.selection_dir)
# for root, dirs, files in os.walk(".", topdown = False):
#    for name in files:

      # print(os.path.join(root, name))
   # for name in dirs:
   #    print(os.path.join(root, name))


# path = ta.selection_dir
# # чтение записей
# with os.scandir(path) as listOfEntries:
#     for entry in listOfEntries:
# # печать всех записей, являющихся файлами
#         if entry.is_file():
#             print(entry.name)