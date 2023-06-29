#Геометрическая прогрессия
a = int(input("Введите первый член прогресси: "))
q = int(input("Введите число на которое умножается предыдущий член прогрессии: "))
n = int(input("Введите количество значений прогрессии: "))
print([a*q**i for i in range(n)])
#Арифмитическая прогрессия
a = int(input("Введите первый член прогресси: "))
q = int(input("Введите число прибавляемое к предыдущему числу прогрессии: "))
n = int(input("Введите количество значений прогрессии: "))
print([a+q*i for i in range(n)])
#Числа Фибоначчи
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
n=int(input("Введите количество элементов последовательности Фибоначи: "))
print(Fibonacci_sequence(n))
#Числа Фибоначчи 2.0
n=int(input("Введите количество элементов последовательности Фибоначи: "))
print([int(((1+5**0.5)**i-(1-5**0.5)**i)/(2**i*5**0.5)) for i in range(1,n+1)])
#Числа Фибоначчи другой способ
n=int(input("Введите количество элементов последовательности Фибоначи: "))
a1=1
a2=1
if n==1:
    print(a1)
elif n==2:
    print(a1,a2)
elif n<=0:
    print('')
elif n>2:
    print(a1,a2,sep='\n')
for i in range(3,n+1):
    a3=a1+a2
    print(a3)
    a1=a2
    a2=a3
#Считает числа Фибоначчи до предела n
def FibonacciList(n, L):
    count = len(L)
    if len(L)<2:# Проверить, корректна ли длина списка
        return []
    num1 = L[count-2]# Получить последние числа в списке L
    num2 = L[count-1]
    if (num1+num2) < n:
        L = L + [num1+num2]# Формула расчета следующего числа
        return FibonacciList(n, L)
    else:
        return L
n=int(input("Введите предел последовательности Фибоначи: "))
print(FibonacciList(n, [0,1]))# Вызвать функцию FibonacciList()
