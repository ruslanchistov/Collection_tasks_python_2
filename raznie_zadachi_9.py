"""Подсчёт повторения слов в текстовом файле"""
import operator
"""Скачиваем текст и записываем отдельными словами в список"""
lst = []
with open('raznie_zadachi_9.txt','r',encoding="utf-8") as f:
    #lst = f.read().split()   Вместо цикла можно написать.
    for line in f:
        for elem in line.split():
            lst.append(elem)

"""Выбираем только буквы без знаков  и делаем буквы строчными"""
lst_2 = []
for i in lst:
    cur = ''
    for simb in i:
        if simb.isalpha() :
            cur += simb.lower()
    lst_2.append(cur)

"""Производим подсчёт количества слов и записываем данные в словарь,
   сортируем в порядке убывания количества повториний"""
dct = {}
for i in lst_2:
    if i != '':
        dct.update({i:lst_2.count(i)})
dct = dict(sorted(dct.items(),key=operator.itemgetter(1),reverse=True))
print(dct)