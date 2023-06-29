import random
animals = []
descriptions = []
print("введите название животного: ")
for i in range(3):
    animal = input()
    animals.append(animal)
print("введите качество животного: ")
for i in range(3):
    description=input()
    descriptions.append(description)
print("вывод смешных сочитаний: ")
for i in range(3):
    print(random.choice(descriptions), random.choice(animals))