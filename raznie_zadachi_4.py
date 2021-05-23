# У вас есть массив чисел, составьте из них максимальное число. Например:
#  [61, 228, 9] -> 961228

# первый вариант:-------------------------------------------
def func(lst):
    count = 1
    while count !=0:
        count = 0
        for i in range(len(lst)-1):
            if (lst[i]+lst[i+1])<(lst[i+1]+lst[i]):
                lst[i],lst[i + 1] = lst[i + 1],lst[i]
                count += 1
    return lst
import random
lst_1 = [random.randint(1,100) for i in range(5)]
print(lst_1)
print(''.join(func(list(map(str,lst_1)))))


# второй вариант:-----------------------------------
class smart_key():
    def __init__(self, obj):
        self.obj = obj
    def __lt__(self, other):
        return (other.obj + self.obj) < (self.obj + other.obj)

max_number = lambda x: ''.join(sorted(map(str, x),key=smart_key))

print(max_number(lst_1))


