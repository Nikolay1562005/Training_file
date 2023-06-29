import os

os.system('pause')

def add(x,y):
    return x + y

def minus(x,y):
    return x - y

def share(x,y):
    return x / y

def multiply(x,y):
    return x * y
it_first = True
while True:
    file = open("Архив операций.txt", "a")
    action=str(input("введите знак операции  (+,-,*,/,c,end): "))
    if action in ('+','-','*','/','c','end'):
        if action == 'end':
            break
        if action != 'c':
            if it_first == 0:
                x = action_user
            else:
                x = float(input("x = "))
            y = float(input("y = "))
            if action == '+':
                print("= " + str(add(x,y)))
                file.write(str(x) + str(action) + str(y) + "=" + str(add(x,y))+ "\n")
                action_user = add(x,y)
            if action == '-':
                print("= " + str(minus(x,y)))
                file.write(str(x) + str(action) + str(y) + "=" + str(minus(x,y))+ "\n")
                action_user = minus(x,y)
            if action == '*':
                print("= " + str(multiply(x,y)))
                file.write(str(x) + str(action) + str(y) + "=" + str(multiply(x,y))+ "\n")
                action_user = multiply(x,y)
            if action == '/' and y != 0:
                print("= " + str(share(x,y)))
                file.write(str(x) + str(action) + str(y) + "=" + str(share(x,y)) + "\n")
                action_user = share(x,y)
            if action == '/' and y == 0:
                print("Ошибка")
                it_first = True
            it_first = False
        else:
            it_first = True
        file.write(str(x) + str(action) + str(y) + "=" + "Ошибка" + "\n")
        file.close()
os.system('pause')
