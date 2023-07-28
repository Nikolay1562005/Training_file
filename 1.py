print('\n', 'Практика 3 Задание 4')
print('введите строку')
print('в строке ДОЛЖНО БЫТЬ! как минимум 6 различных символов различной частоты')
stroka = input()


def zamena3(s):
    global hasto, redko  # чтобы использовать переменные созданные вне функции нужно сделать их общими
    t = ([(s.count(i), i) for i in s if i != ' '])
    hasto = (sorted(set(t))[::-1][:3])
    redko = (sorted(set(t))[::1][:3])
    print('3 самых частых символа в строке')
    print(hasto)
    print('3 самых редких символа в строке')
    print(redko)
zamena3(stroka)
simv = list(stroka)  # split не может делить посимвольно она используется с разделителем а ничто не может быть разделителим так что list делит по символам
print(simv)
for index, item in enumerate(simv):
    for i in range(3):
        a = hasto[i][1] # у Вас был список с массивами поэтому нужно ещё было использовать вызов и из масива
        b = redko[i][1]
        if item == a:
           simv[index] = b
print(''.join(simv))