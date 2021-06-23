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

switcher = 0
# 1 - работа с демо базой, 0 - работа с основной базой
if switcher == 1:
    # исходное местоположение отчётов/автоматов от И.М,
    path_to_table = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/12_sourceProjectAvtomat/'
    output_path = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
    # выборка для  АЦ по изменению средней цены за весь период существования автоматов
    output_name = 'complete_test.xlsx'
    output_name_sheet = 'proba'

else:
    # исходное местоположение отчётов/автоматов от И.М,
    path_to_table = 'X:/аналитика/Отчеты/Автоматы по конкурентам/'
    output_path = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
    output_name = 'filter_free_sales.xlsx'
    output_name_sheet = 'date'

# print(path_to_table, output_path, output_name, output_name_sheet, sep='\n')
# путь к папке содержащей папки с АВТОМАТАМИ
dirs = os.listdir(path_to_table)
date_formatter = "%d.%m.%y"
name_base = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/filter_free_sales.xlsx'

# print(dirs)
# список папок в рабочей папке+
full_path_to_dirs = mf.path_to_dirs(dirs, path_to_table)
#  список путей к файлам
full_list_files = mf.list_files_source(full_path_to_dirs)

#  чтение файла со старыми даннными
old_list = pd.read_excel(name_base, engine='openpyxl', sheet_name='date')
# получение списка уникальных дат
old_list_date = set(old_list.loc[:, 'Дата'])
# получение разницы между старыми данными и новыми выгрузками
dif_list_date = list(set(dirs) - set(old_list_date))
# возвращает полный список новых файлов с путями в папке АВТОМАТ
dif_table_path = mf.list_files_source(mf.path_to_dirs(dif_list_date, path_to_table))
# создаеёт новый dataFrame для добавления к существующей базе
dif_table = mf.full_book_excel_select(dif_table_path)

# выгрузка в имеющийся файл, с перезаписью поверх старых данных
mf.add_print_to_excel(name_base, dif_table)
