import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# anime = pd.read_csv('C:/Users/Козловский/Documents/archive/anime.csv')
# rating = pd.read_csv('C:/Users/Козловский/Documents/archive/rating.csv')
# print(anime.tail(10))
# path_to_table = 'X:/аналитика/Отчеты/Автоматы по конкурентам/'
# table_date = '01.02.21'
# table_name = '/'+'newAvtomatNTM'
# table_ext = '.xlsx'
# full_name = path_to_table+table_date+table_name+table_ext
# file_name = 'X:/аналитика/Отчеты/Автоматы по конкурентам/01.02.21/newAvtomatNTM.xlsx'
# my_table = pd.read_excel(io=file_name,  engine='openpyxl', sheet_name='ОБЪЕКТЫ')
# my_table = pd.read_excel(io='X:/аналитика/Отчеты/Автоматы по конкурентам/01.02.21/newAvtomatNTM.xlsx',  engine='openpyxl', sheet_name='ОБЪЕКТЫ')

# print(my_table.tail(10))

# print(my_table.columns)


df = pd.read_csv('C:/Users/Козловский/Documents/apple.csv', index_col='Date', parse_dates=True)
df = df.sort_index()

# print(df.info())
# print(df.tail(10))
new_sample_df = df.loc['2012-Feb':'2017-Feb', ['Close']]
new_sample_df.plot()
plt.show()