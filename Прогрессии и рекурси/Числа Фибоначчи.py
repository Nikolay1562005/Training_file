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
