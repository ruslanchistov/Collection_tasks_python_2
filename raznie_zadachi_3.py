# Вычислите первые 100 чисел Фибоначчи.
# первый вариант:
fib = [1,1]
for i in range(2,101):
    fib.append(fib[i-1]+fib[i-2])
print(fib)

# второй вариант:
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(101):
    print(fib(i))

# третий вариант:
def fib(n):
    a=b=1
    for i in range(n):
        yield a
        a, b = b, a + b

for i in fib(101):
    print(i)