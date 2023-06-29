from pprint import pprint
goods = [
    {'name': 'iphone 10',
     'brand': 'Apple',
     'price': 50_000
     },
    {'name': 'Samsung A2',
     'brand': 'Samsung',
     'price': 140_000
     },
    {'name': 'iphone 10',
     'brand': 'Apple',
     'price': 50_000
     },
    {'name': 'REALME HL1',
     'brand': 'REALME',
     'price': 30_000
     },
]
print(__name__)
if __name__ == '__main__':
    pprint(sorted(goods, key=lambda item: item['price']))
    apple_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
    print(*apple_list, sep='\n', end='\n\n\n')
    names = ['Иван', 'Миша', 'Кирил']
    surnames = ["Иванов", 'Петров', 'Сидоров']
    patronymic_list = ['Петрович', 'Иванович', 'Михайлович']
    full_names = list(map(lambda name, surname, patronymic:
                         f'Вы: {surname} {name} {patronymic}', names, surnames, patronymic_list))
    print(*full_names, sep="\n")

    indexes_list = []
    k = 0
    for i in goods:
        indexes_list.append({k: i})
        k += 1
    print(*indexes_list, end='\n\n', sep='\n')
    print(list(zip(names, surnames, patronymic_list)))
    for name in zip(names, surnames, patronymic_list):
        print(name)
    a = 45769
    b = filter(lambda item: item['brand'] == 'Apple', goods)
    print(b)