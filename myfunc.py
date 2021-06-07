import os
import datetime

# def date_str_to_date(any_list, format_template):
#     # func форматирования исходного списка
#     nu_list = []
#     for i in any_list:
#         i = datetime.datetime.strptime(i, format_template).date()
#         nu_list.append(i)
#         nu_list.sort(reverse=True)
#     return nu_list
#
# def delete_extension(any_list):
#     # func форматирования исходного списка удаление расширения у файлов
#     nu_list = []
#     for i in any_list:
#         i = i[0:8:1]
#         # применён срез
#         nu_list.append(i)
#         nu_list.sort(reverse=True)
#     return nu_list

def date_str_to_date_and_delete_extension(any_list, format_template):
    # func форматирования исходного списка
    nu_list = []
    for i in any_list:
        if len(i) > 8:
            i = i[0:8:1]
        i = datetime.datetime.strptime(i, format_template).date()
        nu_list.append(i)
        nu_list.sort(reverse=True)
    return nu_list