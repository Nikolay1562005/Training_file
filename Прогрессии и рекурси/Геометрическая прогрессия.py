#РЕШЕНИЕ№1-1
def geom_prog(n, q, arr):
    arr.append(arr[-1] * q)
    return arr if n == 1 else geom_prog(n - 1, q, arr)
n = int(input())
a = int(input())
q = int(input())
arr = [a]
print( geom_prog(n, q, arr))

#РЕШЕНИЕ №1-2
def geom_prog(a, q, n, res=[]):
    if n == 0:
        return res + [a]
    return geom_prog(a*q, q, n-1, res+[a])
print(geom_prog(3, 2, 10))

#РЕШЕНИЕ№1-3
def geom_prog (b,q,n):
    return [b] + [x * q for x in geom_prog(b, q, n-1)] if n > 1 else [b]
print( geom_prog(3,2,10))
