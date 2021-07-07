# СОЗдание пустой базы данных
# def print_to_sql(a):
#     # b - обрабатываемая таблица, список полных путей с именами файлов
#     'X:/аналитика/Отчеты/Автоматы по конкурентам/14.04.21/newAvtomatYAR.xlsx'
#     # a - путь к папке вывода, место где будет расположен итоговый файл эксель
#     # create excel writer object
#     # df = pd.read_excel(io=a, engine='openpyxl', sheet_name='date')
#     df = pd.read_csv(a, encoding='cp1251')
#     table = df.loc[:]
#
#     # print(table)
#
#     cxn = sqlite3.connect(name_db)
#     print(cxn)
#     sql_table = table.to_sql(name_db, con=cxn, if_exists='replace', index=False)
#     cxn.commit()
#     cxn.close()
#     print(sql_table)
#     # table.to_csv(name_csv, sep='|', encoding='cp1251')
#     print('DataFrame is written successfully to Excel File.')
#
#
# print_to_sql(name_csv)
#
# conn = sqlite3.connect(name_db)
# ccc = conn.cursor()
# # print(c)
#
# ccc = ccc.execute("SELECT * FROM filter_free_sales")
#
# results = ccc.fetchall()
# print(ccc)
