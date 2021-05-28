import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path_to_table = 'X:/аналитика/Отчеты/Автоматы по конкурентам/'
table_date = '01.02.21'
table_name = '/'+'newAvtomatNTM'
table_ext = '.xlsx'
full_name = path_to_table+table_date+table_name+table_ext
file_name = 'X:/аналитика/Отчеты/Автоматы по конкурентам/01.02.21/newAvtomatNTM.xlsx'
my_table = pd.read_excel(io=file_name,  engine='openpyxl', sheet_name='ОБЪЕКТЫ')
# my_table = pd.read_excel(io='X:/аналитика/Отчеты/Автоматы по конкурентам/01.02.21/newAvtomatNTM.xlsx',  engine='openpyxl', sheet_name='ОБЪЕКТЫ')

# print(my_table.tail(10))
# print(my_table.columns)
# df = pd.read_csv(full_name, index_col='Date', parse_dates=True)
# df = df.sort_index()

# print(df.info())
# print(df.tail(10))
# new_sample_df = df.loc['2012-Feb':'2017-Feb', ['Close']]
# new_sample_df.plot()
# plt.show()
# print(my_table.columns)
nu_table = my_table.loc[:, ['Комнатность для сайта', 'площадь', 'доступность к продаже',
       'стоимость', 'Цена за м²', 'Статус', 'ID квартиры']]
# nu_table_1 = my_table.loc[:, ['Комнатность для сайта', 'доступность к продаже', 'Статус']]
nu_table = nu_table.loc[nu_table.loc[:,'доступность к продаже'] == 1 ]
nu_table[['date']] = table_date
nu_table[['Проект']] = 'НТ'
ntm_group = nu_table.groupby('Комнатность для сайта').count()
# nu_table.drop(nu_table.drop(nu_table.index, inplace=True))
# print(nu_table.tail(10))
output_path = 'X:/аналитика/КозловскийАВ/10_PYTHON/'
output_name = 'NTM.xlsx'

# create excel writer object
doc_to_excel = pd.ExcelWriter(output_path+output_name)
# write dataframe to excel
nu_table.to_excel(doc_to_excel, '01.01.2020', index=False)
       # save the excel
doc_to_excel.save()


print('DataFrame is written successfully to Excel File.')


# print(ntm_group)