print('Задание 1')
#Как в списке поменять мороженое на шоколад?
spisok = ['хлеб', 'масло', 'мороженое', 'кетчуп']
spisok[2]='шоколад'
print(spisok)

print('Задание 2')
#Запишите какой индекс имеет последний элемент массива A?
A = [8]*7
print('Инекс = ' + str(len(A)-1))

print('Задание 3')
'''Требуется заполнить массив именно так:
X = [1 3 5 7 9 11]
Какой оператор надо поместить в тело цикла вместо многоточия?'''
x=[0]*6
for k in range(6):
    x[k]=2*k+1
print(x)

print('Задание 4')
'''Требуется заполнить массив именно так:
X = [12 9 6 3 0 -3]
Какой оператор надо поместить в тело цикла вместо многоточия?'''
X = [0]*6
for k in range(6):
    X[k] = 12 - 3*k
print('5. X[k] = 12 - 3*k')
print(X)

print('Задание 5')
'''Требуется заполнить массив именно так:
X = [0 3 4 7 8 11]
Какой оператор надо поместить в тело цикла вместо многоточия?'''
X = [0]*6
for k in range(6):
    X[k] = 2*k + k % 2
print('2. X[k] = 2*k + k % 2')
print(X)

list=["колбаса","молоко","чай","пиченье","каша"]
print(list)
list.pop(2)#удаление третьего элемента
print(list)
print("количество элементов: " + str(len(list)))
list.sort()#сортировка по алфавиту или по возрастанию если числа
print(list)
list.pop(len(list)-1)#удаление последнего элемента через функцию длины списка
print(list)


# Выводит значения дву вложенных списков
a=[[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for k in range(len(a[i])):
        print(a[i][k],end=" ")
    print()

# Заполняет список скомандной строки
a = [0] * int(input())
for i in range(len(a)):
    a[i] = int(input())

# Реверс списка
print(sorted( list,reverse = True))



# Счёт элементов списка
list=[1, 2, 3, 4, 5]
s=sum(list)
print(s)
list_length=len(list)
sumOfElements=0

# програмный аналог
for i in range(list_length):
    sumOfElements=sumOfElements+list[i]
print(sumOfElements)

# Считает сумму натуральных чисел до определённого
def summa_n(n):
    rez_sum=0
    for i in range(n+1):
        rez_sum=rez_sum + i
    return int(rez_sum)
n=int(input("Введите число: "))
print(summa_n(n))