# Напишите функцию, которая создаёт комбинацию двух списков таким образом:
# [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]

import random
lst_1 =[random.randint(1,10) for i in range(10)]
lst_2 =[random.randint(11,25) for i in range(10)]
print(lst_1)
print(lst_2)

# первый вариант:
print(sum(zip(lst_1,lst_2),()))

# второй вариант:
if len(lst_1)>=len(lst_2):
    for idx,var in enumerate(lst_2) :
        lst_1.insert(idx*2,var)
    print(lst_1)
else:
    for idx,var in enumerate(lst_1):
        lst_2.insert(idx*2,var)
    print(lst_2)
