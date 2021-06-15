import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

# скрип берёт в NewAvtnomat файл эксель, убирает лишние столбцы, фильтрует по доступности к продаже
# и создаёт новый файл с 5ю столбцами и произведённой фильтрацией
# в файле создаеёт лист с датой куда и помещает выжимку

pd.set_option('display.max_rows', 1000000)
pd.set_option('display.max_columns', 1000000)
pd.set_option('display.width', 1000000)
pd.options.display.float_format = '{:.2f}'.format


# path_to_table = 'X:/аналитика/Отчеты/Автоматы по конкурентам/'
# table_date = '31.05.21'
# table_name = '/' + 'newAvtomatNTM'
# table_ext = '.xlsx'
# full_name = path_to_table + table_date + table_name + table_ext
# file_name = 'X:/аналитика/Отчеты/Автоматы по конкурентам/31.05.21/newAvtomatNTM.xlsx'
# my_table = pd.read_excel(io=file_name, engine='openpyxl', sheet_name='ОБЪЕКТЫ')
my_table = pd.read_excel(io='X:/аналитика/Отчеты/Автоматы по конкурентам/19.05.21/newAvtomatTOP.xlsx',  engine='openpyxl', sheet_name='ОБЪЕКТЫ')
# print(my_table.tail(10))
print(my_table.columns)
# nu_table = my_table.loc[:, ['Комнатность для сайта', 'доступность к продаже', 'Статус']]
# print(nu_table)
# ntm_group = nu_table.groupby('Комнатность для сайта').count()
# print(ntm_group)
# nu_table.drop(nu_table.drop(nu_table.index, inplace=True))
# print(nu_table.tail(10))



#
# # работающий базовый скрипт для выгрузки в эксель
#
# nu_table = my_table.loc[:, ['Комнатность для сайта', 'площадь', 'доступность к продаже',
#                             'стоимость', 'Цена за м²', 'Статус', 'ID квартиры']]
#
# nu_table = nu_table.loc[nu_table.loc[:, 'доступность к продаже'] == 1]
# nu_table[['date']] = table_date
# project_name = 'МК'
# nu_table[['Проект']] = project_name
# print(nu_table)
#
# output_path = 'X:/аналитика/КозловскийАВ/06_ТУРНИРАЯ ТАБЛИЦА/13_finalProject/'
# output_name = 'NTM02.xlsx'
# # create excel writer object
# doc_to_excel = pd.ExcelWriter(output_path+output_name)
# # write dataframe to excel
# nu_table.to_excel(doc_to_excel, project_name , index=False)
# # save the excel
# doc_to_excel.save()
#
# print('DataFrame is written successfully to Excel File.')
