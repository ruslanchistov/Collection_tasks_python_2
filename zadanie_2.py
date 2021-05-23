# Проверить, есть ли в последовательности дубликаты

import random
list_1 =[random.randint(1,300) for i in range(20)]
print(list_1)
if len(list_1) != len(set(list_1)):
    print('Дубликаты есть')
else:
    print('Дубликатов нет')