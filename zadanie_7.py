# Требуется создать функцию list_sort(lst),
# которая сортирует список чисел по убыванию их абсолютного значения.

def list_sort(lst):
    lst.sort(key = lambda i : abs(i),reverse=True)
    return lst

import random
List = [random.randint(-20, 20) for i in range(15)]
print(List)
List = list_sort(List)
print(List)