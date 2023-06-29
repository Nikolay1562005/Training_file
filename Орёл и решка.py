import random
user_choice=str(input("Введите орёл или решка "))
computer_choice=random.randint(0,1)
if computer_choice == 1:
    computer_choice="орёл"
else:
    computer_choice="решка"
if user_choice == computer_choice:
        print("золотая карта")
else:
    print("100$")
print(computer_choice)
