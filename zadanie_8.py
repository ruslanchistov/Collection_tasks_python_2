# На входе имеем список строк разной длины.
# Необходимо написать функцию all_eq(lst), которая вернет новый список из строк одинаковой длины.
# Длину итоговой строки определяем исходя из самой большой из них.
# Если конкретная строка короче самой длинной,
# дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов.
# Расположение элементов начального списка не менять.

# Первый вариант:
def all_eq_1(lst):
    max_str = len(max(lst))
    for idx,elem in enumerate(lst):
        if len(elem) < max_str:
            elem += '_'*(max_str - len(elem))
            lst[idx] = elem
    return lst

# Второй вариант:
def all_eq_2(lst):
    max_str = len(max(lst))
    return [item.ljust(max_str, '_') for item in lst]

import random
lst =['a'* random.randint(1,7) for i in range(10)]
print(lst)
print(all_eq_1(lst))
print(all_eq_1(lst))