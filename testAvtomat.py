import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

import myfunc as mf

selection_dir = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/12_sourceProjectAvtomat/'
# исходное местоположение отчётов/автоматов от И.М,

final_dir = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
# финальное размещение выходных файлов

dirs = os.listdir(selection_dir)
files = os.listdir(final_dir)
# содержимое папки
#  list имен папок из исходного местоположения, даты в строк. формате

date_formatter = "%d.%m.%y"
# шаблон форматированиz дат
# dirs_0 = datetime.datetime.strptime(dirs[0], date_formatter).date()

extens='.xlsx'
# удаляемое расширение

dir_contain = selection_dir+dirs[0]
# print(dir_contain)
files_into_dir = os.listdir(dir_contain)


source_list = mf.date_str_to_date_and_delete_extension(dirs, date_formatter)
final_list = mf.date_str_to_date_and_delete_extension(files, date_formatter)

# print(source_list)
# обработанные списки
# print(mf.date_str_to_date_and_delete_extension(dirs, date_formatter))
# print(mf.date_str_to_date_and_delete_extension(files, date_formatter))


# сравнение 2ух списков и составление третьего, в котором элементы отсутствующие во 2 списке
list_difference = set(source_list) - set(final_list)
# print(list_difference)



# из исходной папки из папки на дату взять список файлов,
# извлечь те листы которые содержат требуемые данные,
# слить в одну базу все листы по проекту,
# получить нужные столбцы и пропустить через нужные фильтры,
# после создать выходной файл на дату датной папки, где каждый лист назван проектом
# куда вносятся все данные, которые полученые отбором и фильтрацией

