n=int(input("Введите количество элементов последовательности Фибоначи: "))
# по формуле из инета
l_1=[int(((1+5**0.5)**i-(1-5**0.5)**i)/(2**i*5**0.5)) for i in range(1,n+1)]
print([int(((1+5**0.5)**i-(1-5**0.5)**i)/(2**i*5**0.5)) for i in range(1,n+1)])

# по формуле из инета с библеотекой
from math import sqrt
l_2=[int(((1+sqrt(5))**i-(1-sqrt(5))**i)/(2**i*sqrt(5))) for i in range(1,n+1)]
print(l_2)

# Классический способ вычисления (эталон)
def Fibonacci_sequence(n):
    if n == 0:
        Fibonacci_numbers=[0]
    elif n == 1:
        Fibonacci_numbers=[1]
    elif n == 2:
        Fibonacci_numbers=[1,1]
    elif n > 2:
        Fibonacci_numbers=[1,1]
        for i in range(2,n):
            Fibonacci_numbers.append(Fibonacci_numbers[i-2]+Fibonacci_numbers[i-1])
    return Fibonacci_numbers
s=Fibonacci_sequence(n)
print(s)

# бойня 1 против эталона
k_1=[]
for i in range(n):# поиск разницы двух списков
    k_1.append(l_1[i]-s[i])
print(k_1)
for i in range(n):
    if k_1[i] != 0:
        print(i+1)#вывод номера первого числа не равного по формуле числу Фиббоначи
        
# бойня 2 против эталона
k_2=[]
for i in range(n):# поиск разницы двух списков
    k_2.append(l_2[i]-s[i])
print(k_2)
for i in range(n):
    if k_2[i] != 0:
        print(i+1)#вывод номера первого числа не равного по формуле числу Фиббоначи

