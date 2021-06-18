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
import constant as ct

# модули регулирующие параметры предстваления вывода при debug
pd.set_option('display.max_rows', 1000000)
pd.set_option('display.max_columns', 1000000)
pd.set_option('display.width', 1000000)
pd.options.display.float_format = '{:.2f}'.format

switcher = 1
# 1 - работа с демо базой, 0 - работа с основной базой
if switcher == 1:
    path_to_table = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/12_sourceProjectAvtomat/'
    output_path = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
    # выборка для  АЦ по изменению средней цены за весь период существования автоматов
    output_name = 'complete_1.xlsx'
    output_name_sheet = 'proba'

else:
    path_to_table = 'X:/аналитика/Отчеты/Автоматы по конкурентам/'
    output_path = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
    output_name = 'complete.xlsx'
    output_name_sheet = 'date'

# print(path_to_table, output_path, output_name, output_name_sheet, sep='\n')



# финальное размещение выходных файлов
final_dir = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
# исходное местоположение отчётов/автоматов от И.М,
# path_to_table = 'X:/аналитика/Отчеты/Автоматы по конкурентам/'
# path_to_table = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/12_sourceProjectAvtomat/'

# входные данные для выгрузки из автоматов Ивана
# avtomat_path_to_table = 'X:/аналитика/Отчеты/Автоматы по конкурентам/'
# avtomat_fin_dir = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
# avtomat_dirs = os.listdir(avtomat_path_to_table)
# avtomat_full_path_to_dirs = mf.path_to_dirs(avtomat_dirs, avtomat_path_to_table)
# avtomat_output_name = 'full_avtomat.xlsx'

# список для финальной обработки
# avtomat_full_list_files = mf.list_files_source(avtomat_full_path_to_dirs)
# table_avtomat = mf.full_book_excel_select(avtomat_full_list_files)

# print(avtomat_full_list_files)
# путь к папке содержащей папки с АВТОМАТАМИ
dirs = os.listdir(path_to_table)
date_formatter = "%d.%m.%y"
# di_date =
# print(dirs)
# список папок в рабочей папке+
full_path_to_dirs = mf.path_to_dirs(dirs, path_to_table)
#  список путей к файлам
full_list_files = mf.list_files_source(full_path_to_dirs)
# print(len(full_path_to_dirs))
# список файлов в папке АВТОМАТОВ
# print(len(full_list_files),*full_list_files, sep='\n')
# print(len(full_list_files))

# print(*mf.xls_sheet(full_list_files, list_for_download), sep='\n')

# list_temp = full_list_files[1]
# list_temp_all = full_list_files[2]
# print(list_temp_all)

# y_table = pd.read_excel(io=list_temp_all, engine='openpyxl')
# print(y_table.columns)

# print(list_temp)
# print(*mf.xls_sheet(list_temp, list_for_download))
# print(mf.concat_list_2(list_temp))
# nu_list = full_list_files[0]
nu_list = full_list_files

# print(nu_list)



# mf.full_book_excel_select(nu_list)
# table = mf.full_book_excel_select(nu_list)
# print(table)
# avtomat_path_to_table = 'X:/аналитика/Отчеты/Автоматы по конкурентам/'
# avtomat_fin_dir = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
# avtomat_dirs = os.listdir(avtomat_path_to_table)
# # print(avtomat_dirs)
# avtomat_full_path_to_dirs = mf.path_to_dirs(avtomat_dirs, avtomat_path_to_table)
# # print(avtomat_full_path_to_dirs)
# avtomat_output_name = 'complete.xlsx'
#
# avtomat_full_list_files = mf.list_files_source(avtomat_full_path_to_dirs)
# print(avtomat_full_list_files, sep='\n')

# принимает массив и выгружает его в эксельный файл
def print_to_excel(a,b,c,d):
    print('hell')
    # a - обрабатываемая таблица, список полных путей с именами файлов 'X:/аналитика/Отчеты/Автоматы по конкурентам/14.04.21/newAvtomatYAR.xlsx'
    # b - путь к папке вывода, место где будет расположен итоговый файл эксель
    # c - нименование выходного файла
    # d - имя листа в создаваемом файле
    # create excel writer object
    doc_to_excel = pd.ExcelWriter(b + c, engine='xlsxwriter')
    # write dataframe to excel
    a.to_excel(doc_to_excel, d, index=False)
    # table.to_excel(doc_to_excel, 'all_projects', index=False)
    # save the excel
    doc_to_excel.save()
    print('DataFrame is written successfully to Excel File.')

table_avtomat = mf.full_book_excel_select(full_list_files)
# print(table_avtomat)

print_to_excel(table_avtomat, output_path, output_name, output_name_sheet)
# print_to_excel(table, output_path, output_name, output_name_sheet )

# # create excel writer object
# doc_to_excel = pd.ExcelWriter(avtomat_fin_dir + avtomat_output_name, engine='xlsxwriter')
# # write dataframe to excel
# table_avtomat.to_excel(doc_to_excel, 'all_projects', index=False)
# # table.to_excel(doc_to_excel, 'all_projects', index=False)
# # save the excel
# doc_to_excel.save()
# print('DataFrame is written successfully to Excel File.')
#
#  # принимает список путей к файлам возворащает список [путь к файлу, дата отчёта,
#  # наименование проекта (по принятым сокращениям - ВБ2, НТ и пр.)]
#
# df_ = pd.DataFrame(data=None, columns=ct.headers_all)
# print(df_)


# empty_table = pd.DataFrame(index=index, columns=ct.headers_all)
# nda1 = np.array([[1, 1, 1, 1, 1, 1], ct.headers_all])
# df4 = pd.DataFrame(nda1)
# print(df4)
# print(empty_table)