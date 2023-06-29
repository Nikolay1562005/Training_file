n=int(input("введите число n больше либо равно 2, но меньше либо равно 1000 = "))
k=int(input("введите число x от 0 до 3 = "))
x=(n-2)*(n-2)*(n-2)
y=(n-2)*(n-2)*6
z=n*n*n-x-y-8
if k == 0:
 print(int(x))
if k == 1:
 print(int(y))
if k == 2:
 print(int(z))
if k == 3:
 print(int(8))
