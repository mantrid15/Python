import requests
import pyodata
import json

# a = 'http://159.69.74.161/nagorny_test/odata/standard.odata?$format=application/json'
a = 'http://192.168.10.110/UPN_BAR/odata/standard.odata/Document_УПН_СделкаПоНедвижимости?$format=application/json'

# $select=Description, 'Комментарий,НаименованиеПолное,СделкаСсылка_Key&

r = requests.get(a)
# r2 = json.loads(r.text)

# d = requests
print(r.text)
