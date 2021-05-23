# 1. Создать множество(set)
# 2. Создать неизменяемое множество(frozenset)
# 3. Выполнить операцию объединения созданных множеств
# 4. Выполнить операцию пересечения созданных множеств

import random
set_1 = set(random.randint(1,100) for i in range(20))
set_2 = frozenset(random.randint(1,100) for i in range(20))
print(set_1)
print(set_2)
set_3 = set_1 | set_2
print('объединение')
print(set_3)
set_4 = set_1 & set_2
print('пересечение')
print(set_4)