# У вас есть массив чисел.
# Напишите три функции, которые вычисляют сумму этих чисел:
# с for-циклом, с while-циклом, с рекурсией.

def for_cicl(lst):
    summa = 0
    for elem in lst:
        summa += elem
    return summa

def while_cicl(lst):
    idx = 0
    summa = 0
    while idx < len(lst):
        summa += lst[idx]
        idx +=1
    return summa

def recursiya(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + recursiya(lst[1:])


import random
lst = [random.randint(1,10) for i in range(15)]
print(lst)
print(sum(lst))
print(for_cicl(lst))
print(while_cicl(lst))
print(recursiya(lst))


