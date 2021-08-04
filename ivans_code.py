import requests
import json
import pandas as pd
import datetime
import shutil
import os
import sys
pd.set_option('display.max_rows', 1000000)
pd.set_option('display.max_columns', 1000000)
pd.set_option('display.width', 1000000)
pd.options.display.float_format = '{:.2f}'.format

json_url = 'http://incrm.ru/export-tred/ExportToSite.svc/ExportToTf/json'
last_file = 'row_data_last.xlsx'


def get_json(url):
    session = requests.session()
    param = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/78.0.3904.108 Safari/537.36',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                       'application/signed-exchange;v=b3'}
    r = session.get(url, headers=param)
    json_data = json.loads(r.text)
    data_frame = pd.DataFrame.from_records(json_data)
    data_frame = data_frame.rename(columns={'Article': 'ID объекта', 'Quantity': 'Площадь', 'Rooms': 'Комнатность '
                                                                                                     '0/1/2/3/4',
                                            'Sum': 'Стоимость', 'Decoration': 'Отделка 0/1/2/3', '2level':
                                                'Двухуровневая 0/1', 'IsEuro': 'ЕвроКвартира 0/1'})
    decoration_text_lst = list(data_frame['Отделка 0/1/2/3'])
    data_frame['Отделка 0/1/2/3'] = data_frame['Отделка 0/1/2/3'].replace({'Без отделки': 0, 'без отделки': 0, 'WhiteBox': 3, 'черновая': 1, 'Черновая': 1, 'Чистовая': 2, 'чистовая': 2, 'Милан': 2, 'Венеция': 2, 'ЯЛТА': 2,
                                                                           'Классика': 2, 'МОДЕРН': 2, 'Рассвет': 2, '': 0, 'Закат': 2, 'Модерн': 2})

    try:
        data_frame['Отделка 0/1/2/3'] = data_frame['Отделка 0/1/2/3'].astype('int')
        data_frame['Площадь'] = data_frame['Площадь'].astype('float')
        data_frame['Комнатность 0/1/2/3/4'] = data_frame['Комнатность 0/1/2/3/4'].astype('int')
        data_frame['Стоимость'] = data_frame['Стоимость'].astype('float')
        data_frame['Двухуровневая 0/1'] = data_frame['Двухуровневая 0/1'].astype('int')
        data_frame['ЕвроКвартира 0/1'] = data_frame['ЕвроКвартира 0/1'].astype('int')
    except ValueError:
        print('Проверьте значения в json:\nКомнатность, ЕвроКвартира, Двухуровневая и Отделка должны быть целыми '
              'числами\nПлощадь, Цена и Стоимость должны быть вещественными числами\n '
              'Скорее всего появились тектовые значения (в том числе пустые)\nКорректная работа прораммы не возможна, '
              'обратитесь к разработчику (*следует обратить внимание на блок try*).')
        sys.exit()
    else:
        data_frame['Цена'] = data_frame['Стоимость'] / data_frame['Площадь']
        data_frame['ОтделкаТекстом'] = decoration_text_lst
        data_frame['ОтделкаТекстом'] = data_frame['ОтделкаТекстом'].replace({'': 'Без отделки'})
        data_frame = data_frame.reindex(columns=['ID объекта', 'StatusCodeName', 'Комнатность 0/1/2/3/4', 'ЕвроКвартира 0/1', 'Двухуровневая 0/1', 'Отделка 0/1/2/3', 'Площадь', 'Цена', 'Стоимость', 'ОтделкаТекстом'])
        return data_frame


def get_last_data(file):
    series = pd.read_excel(file, sheet_name='row_data_last')
    data_frame = pd.DataFrame.from_records(series, columns=['ЖК', 'ID объекта', 'ID 1C', 'Корпус факт', 'Корпус 1С', 'Корпус счёт сайт', 'Предназначение', 'Секция', 'Этаж', 'Номер на этаже', 'Условный номер', 'Статус 0/1', 'Комнатность 0/1/2/3/4',
                                                            'ЕвроКвартира 0/1', 'Двухуровневая 0/1', 'Отделка 0/1/2/3', 'Площадь', 'Цена', 'Стоимость', 'СпециальнаяСтоимость', 'ОтделкаТекстом'])
    return data_frame


def copy_last_file():
    date = datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
    dir_of_base_file = 'C:\\ProjectsM\\full_row_data\\'
    dir_of_copy_file = 'C:\\ProjectsM\\full_row_data\\Резервное копирование\\'
    path_to_base_file = dir_of_base_file + last_file
    shutil.copy2(path_to_base_file, dir_of_copy_file)
    path_to_copy_file = dir_of_copy_file + last_file
    new_path_name_of_copy_file = dir_of_copy_file + 'row_data_last_' + date + '.xlsx'
    os.rename(path_to_copy_file, new_path_name_of_copy_file)


print('Программа осуществляет запрос к источникам данных, подождите...')
data_frame_from_json = get_json(json_url)
data_frame_from_last_file = get_last_data(last_file)
print('\nДанные из json-файла застройщика и последнего xlsx-исходника успешно считаны!\n')
try:
    copy_last_file()
except OSError:
    print('\nВозникли проблемы с копированием данных из последнего исходника, обратитесь к разработчику!')
else:
    print(r'Данные из последнего исходника скопированы в папку C:\ProjectsM\full_row_data\Резервное копирование')

print('\nДанные в исходнике обновляются, подождите...')
static_cols = ['ЖК', 'ID объекта', 'ID 1C', 'Корпус факт', 'Корпус 1С', 'Корпус счёт сайт', 'Предназначение', 'Секция', 'Этаж', 'Номер на этаже', 'Условный номер']
dynamic_cols = ['Комнатность 0/1/2/3/4', 'ЕвроКвартира 0/1', 'Двухуровневая 0/1', 'Отделка 0/1/2/3', 'Площадь', 'Цена', 'Стоимость']   # Столбец Статус 0/1 заполняется по особому правилу

new_data = pd.DataFrame()

for col in static_cols:
    new_data[col] = data_frame_from_last_file[col]
new_data['Статус 0/1'] = ['' for j in range(len(new_data['ID объекта']))]
for col in dynamic_cols:
    new_data[col] = ['' for j in range(len(new_data['ID объекта']))]

lst_obj_from_json = list(data_frame_from_json['ID объекта'])
for i in range(len(new_data['ID объекта'])):
    code = new_data['ID объекта'][i]
    if code in lst_obj_from_json:
        code_index_from_json = data_frame_from_json[data_frame_from_json['ID объекта'] == code].index[0]
        if data_frame_from_json['StatusCodeName'][code_index_from_json] == 'Свободно' or data_frame_from_json['StatusCodeName'][code_index_from_json] == 'Ус. Бронь':
            new_data.loc[i, 'Статус 0/1'] = 1
            for col in dynamic_cols:
                new_data.loc[i, col] = data_frame_from_json[col][code_index_from_json]
        else:
            new_data.loc[i, 'Статус 0/1'] = 0
            for col in dynamic_cols:
                new_data.loc[i, col] = data_frame_from_last_file[col][i]
    else:
        new_data.loc[i, 'Статус 0/1'] = 0
        for col in dynamic_cols:
            new_data.loc[i, col] = data_frame_from_last_file[col][i]

zubik_sum_lst = list()
data_frame_from_json_id_obj_lst = list(data_frame_from_json['ID объекта'])
for j in range(len(new_data['ID объекта'])):
    if new_data['ID объекта'][j] in data_frame_from_json_id_obj_lst and data_frame_from_json[data_frame_from_json['ID объекта'] == new_data['ID объекта'][j]]['StatusCodeName'].values[0] == 'Свободно':
        zubik_sum_lst.append(new_data['Стоимость'][j])
    else:
        zubik_sum_lst.append(data_frame_from_last_file[data_frame_from_last_file['ID объекта'] == new_data['ID объекта'][j]]['СпециальнаяСтоимость'].values[0])
new_data['СпециальнаяСтоимость'] = zubik_sum_lst

text_decoration_lst = list()
data_frame_from_json_id_obj_lst = list(data_frame_from_json['ID объекта'])
for j in range(len(new_data['ID объекта'])):
    if new_data['ID объекта'][j] in data_frame_from_json_id_obj_lst and (data_frame_from_json[data_frame_from_json['ID объекта'] == new_data['ID объекта'][j]]['StatusCodeName'].values[0] == 'Свободно' or
                                                                         data_frame_from_json[data_frame_from_json['ID объекта'] == new_data['ID объекта'][j]]['StatusCodeName'].values[0] == 'Ус. Бронь'):
        text_decoration_lst.append(data_frame_from_json[data_frame_from_json['ID объекта'] == new_data['ID объекта'][j]]['ОтделкаТекстом'].values[0])
    else:
        text_decoration_lst.append(data_frame_from_last_file[data_frame_from_last_file['ID объекта'] == new_data['ID объекта'][j]]['ОтделкаТекстом'].values[0])
new_data['ОтделкаТекстом'] = text_decoration_lst


ad_price_dict = {'квартира': 30000, 'апартаменты': 30000, 'кладовая': 10000, 'машиноместо': 15000, 'коммерческое': 30000, 'нж': 30000}
ad_price_br_dict = {'квартира': 50000, 'кладовая': 30000, 'машиноместо': 30000}
price_plus_ad_lst = list()
for i in range(len(new_data['Стоимость'])):
    if new_data['ЖК'][i] == 'БР':
        price_plus_ad_lst.append(new_data['Стоимость'][i] + ad_price_br_dict[new_data['Предназначение'][i]])
    else:
        price_plus_ad_lst.append(new_data['Стоимость'][i] + ad_price_dict[new_data['Предназначение'][i]])
new_data['СтоимсотьВключаяАД'] = price_plus_ad_lst

try:
    writer = pd.ExcelWriter(last_file, engine='xlsxwriter')
    new_data.to_excel(writer, sheet_name='row_data_last', index=False)
    workbook = writer.book
    worksheet = writer.sheets['row_data_last']
    number_format = workbook.add_format({'num_format': '#,##0.00'})
    worksheet.set_column('B:B', 23)
    worksheet.set_column('Q:T', 23, number_format)
    worksheet.set_column('U:U', 23)
    worksheet.set_column('V:V', 23, number_format)
    writer.save()
    shutil.copy2('C:\\ProjectsM\\full_row_data\\row_data_last.xlsx', 'X:\\Аналитика\\Отчеты\\!Шахматки и прогнозы\\price\\')
except PermissionError:
    print('\nЗакройте файл row_data_last.xlsx и запустите прорамму ещё раз (файл может быть открыт у другого пользователя)')
