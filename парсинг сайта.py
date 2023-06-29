import requests
import random
from bs4 import BeautifulSoup

def fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response,'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    print(fact.text)
    print(fact.a.attrs['href'])
i = input("Хотите рандомный факт: ")
while i == "да" or i == "Да" or i == "yes" or i == "Yes":
    fact()
    i = input("Хотите рандомный факт: ")
else:
    print(':(')

'''
response = requests.get('https://i-fact.ru/')
response = response.content
html = bs4.BeautifulSoup(response, 'lxml')
fact = random.choice(html.find_all(class_='p-2 clearfix'))
print(fact.text)
print(fact.a.atters['href'])
'''