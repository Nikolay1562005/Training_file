k = int(input("Введите значение: "))
#---1---
def f(n):
    d = []
    if n < 0 or n == 0 or n == 1: return d
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            d.append(i)
            d.append(int(n/i))
    d.sort()
    return d


if len(f(k)) == 2:
    print(f'Число {k} - простое')
else:
    print(f'Число {k} - составное')

#---2---
def IsPrime_1(n):
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        t = 'простое'
    else:
        t = "составное"
    return f'Число {n} - {t}'

print(IsPrime_1(k))

#---3---
def IsPrime_2(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    if d * d > n:
        t = 'простое'
    else:
        t = "составное"
    return f'Число {n} - {t}'

print(IsPrime_2(k))

#---4---
def IsPrime_3(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    if (d * d > n)==1:
        t = 'простое'
    else:
        t = "составное"
    return f'Число {n} - {t}'

print(IsPrime_3(k))