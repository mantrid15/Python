import pyodata
import requests
import json
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 1000000)
pd.set_option('display.max_columns', 1000000)
pd.set_option('display.width', 1000000)
pd.options.display.float_format = '{:.2f}'.format


r = requests.get('http://192.168.10.110/OBL/odata/standard.odata/Task_ЗадачаИсполнителя?$top=1&$format=json', auth=('seo', '3052007'), verify=True)
# r = requests.get('http://192.168.10.110/OBL/odata/standard.odata/Task_ЗадачаИсполнителя?$select=Description, Date, '
#                  'ДатаИсполнения, ДатаПринятияКИсполнению, Предмет, ПредметСтрокой, РезультатВыполнения, '
#                  'АвторСтрокой, Исполнитель, РольИсполнителя &$format=json', auth=('seo', '3052007'), verify=True)
# json_data = r.json()
json_data = json.loads(r.text)

print(json_data)
# data_frame = pd.DataFrame(json_data).loc[:, 'value']
data_frame = pd.DataFrame(json_data).loc[:, 'value']
# nudata = pd.DataFrame(data_frame)
# data_frame = pd.DataFrame.from_records(json_data).loc[:, 'value']
# data_frame = pd.DataFrame(json_data['value'][1], columns=json_data['value'][0])
# print(data_frame)

# data_series = pd.Series(data_frame)
# print(data_series)
array = []
for i in data_frame:

    array += i.items()

    # print(i)
# print(array)

# nulist = array.tolist()

# print(len(array))

# print(nudata)
# odata_headers = ['Description',
#                  'Date',
#                  'ДатаИсполнения',
#                  'ДатаПринятияКИсполнению',
#                  'Предмет',
#                  'ПредметСтрокой',
#                  'РезультатВыполнения',
#                  'АвторСтрокой',
#                  'Исполнитель',
#                  'РольИсполнителя']


# SERVICE_URL = 'http://192.168.10.110/OBL/odata/standard.odata/Task_ЗадачаИсполнителя'
# path = requests.get('http://192.168.10.110/OBL/odata/standard.odata/Task_ЗадачаИсполнителя', auth=('seo', '3052007'))
# # session = requests.Session()
# # session.auth = ('seo', '3052007')
#
# # one_data = pyodata.Client(SERVICE_URL, session)
# # print(type(one_data))
#
# r = requests.get(path)
# data = r.json()
# df = pd.DataFrame(data).loc[:]
# print(df)
# data_frame = pd.DataFrame(one_data).loc[:, 'value']
# data_frame = pd.DataFrame.from_records(json_data).loc[:, 'value']
# data_frame = pd.DataFrame(json_data['value'][1], columns=json_data['value'][0])
# print(data_frame)
# print(one_data)

# # r = requests.get('http://192.168.10.110/OBL/odata/standard.odata/Task_ЗадачаИсполнителя?$select=Description, Date, '
#                  'ДатаИсполнения, ДатаПринятияКИсполнению, Предмет, ПредметСтрокой, РезультатВыполнения, '
#                  'АвторСтрокой, Исполнитель, РольИсполнителя &$format=json ',
# #                  auth=('seo', '3052007'), verify=True)
# r = requests.get('http://192.168.10.110/OBL/odata/standard.odata/Task_ЗадачаИсполнителя?$select=Description, '
#                  'Date &$format=json', auth=('seo', '3052007'), verify=True)
# session = requests.session()