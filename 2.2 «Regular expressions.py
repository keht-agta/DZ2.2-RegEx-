import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# 1. Поместить Фамилию, Имя и Отчество человека в поля `lastname`, `firstname` и `surname` соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О. 
###### Изменяем список контактов разбивая ФИО, Ф+ИО, на Ф+И+О
for i, contact in enumerate(contacts_list):
    temp_list = contact[:3]
    for element in temp_list[::1]:
        temp_list.extend(element.split())
    if len(temp_list) < 6:
        temp_list.append('')
    contacts_list[i][0],contacts_list[i][1],contacts_list[i][2] = temp_list[3],temp_list[4],temp_list[5]
# 2. Привести все телефоны в формат +7(999)999-99-99. 
# Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999. _Подсказка: используйте регулярки для обработки телефонов_.
# pattern = r"(\+7|8)(\s*)?(\()?(\d{3})(\D*)?(\d{3})(\D*)(\d{2})(\D*)(\d{2})(\s\(?)?(доб.)?(\s?)(\d*)?"
pattern = r'(\+7|8)(\s*)?(\()?(\d{3})(\D*)?(\d{3})(\D*)(\d{2})(\D*)(\d{2})(\s\(?)?(доб\.)?(\s)?(\d*)?(\D*)?'
sub_pattern = r"+7(\4)\6-\8-\10 \12\14"
for i, contact in enumerate(contacts_list):
    contact[5] = re.sub(pattern, sub_pattern, contact[5])
#3 3. Объединить все дублирующиеся записи о человеке в одну. _Подсказка: группируйте записи по ФИО (если будет сложно, допускается группировать только по ФИ)_.
    # 1- найти +
    # 2 объединить +
    # 3 удалить не нарушив массив???
# 1 найти. Запускаем цикл по всем конаткам и сравниваем контакт со всеми остальными. ПРи нахождении объединяем и делаем контакты одинаковыми.
for i, contact in enumerate(contacts_list):
    for j in range(i+1,len(contacts_list)):
        if contact[:2] == contacts_list[j][:2]:
            for k in range(2,len(contact)):
                if not contact[k]:
                    contact[k]=contacts_list[j][k]
                else:
                    contacts_list[j][k]=contact[k]
# 3 удалить не нарушив массив, путем создания нового и добавления не повторяющихся.
res = []
[res.append(x) for x in contacts_list if x not in res]

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(res)