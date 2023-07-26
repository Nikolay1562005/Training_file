goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
stores ={
    '12345': [
        {'quantity': 27, 'price': 42},
        ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
        ],
    '34567': [
        {'quantity': 2,'price': 1200},
        {'quantity': 1,'price': 1150}
        ],
    '45678': [
        {'quantity': 50,'price': 100},
        {'quantity': 12,'price': 95},
        {'quantity': 43,'price': 97},
        ],
}
print("Введите название товара: ")
good=input()
quantity_good=0
if good in goods:
    quantity_good = 0
    good_stores=stores[goods[good]] #список из словаря stores  
    all_price=0
    for number_for_list  in range(len(good_stores)):
        quantity_good=quantity_good + int(good_stores[number_for_list]["quantity"])                                   #считает количество товара на складах
        all_price=all_price+int(good_stores[number_for_list]["price"])*int(good_stores[number_for_list]["quantity"])  #считает сумму на которую находится товара на складе + предыдущее значение
    print(str(good) + " - " + str(quantity_good) + " шт, стоимость " + str(all_price) + "руб")
else:
    Print("товара нет на складе")