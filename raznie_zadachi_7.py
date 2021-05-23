# Какое наименьшее положительное число делится без остатка на все числа от 1 до 20?
# Вычисление очень долгое, ответ 232792560.
num = 20
count = 0
while True:
    for i in range(1,21):
        if num % i != 0:
            count += 1
    if count == 0:
        print (num)
        break
    count = 0
    num += 20

