# Напишите функцию change(lst), которая принимает список
# и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

def func(LIST):
    LIST[0],LIST[-1] = LIST[-1],LIST[0]
    return(LIST)
import random
List = [random.randint(1,20) for i in range(15)]
print(List)
List = func(List)
print(List)