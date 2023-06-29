from tkinter import *
import requests
import random
import bs4
import lxml

window = Tk()
window.geometry('700x600')

'''def get_content():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = bs4.BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    print(fact.text)
    print(fact.a.attrs['href'])'''


def draw_menu():
    clear()
    label_title = Label(text='Что бы вы хотели сделать? ', font=('Arial', 24), fg='white', bg='orange')
    label_title.place(width=700, height=50, x=0, y=0)
    b1 = Button(text='Узнать что-то новое', font=('Arial', 18), fg='black', command=clear)
    b1.place(x=25, y=75, width=300)
    b2 = Button(text='Смотреть на котиков', font=('Arial', 18), fg='black', command=clear)
    b2.place(x=375, y=75, width=300)


def clear():
    all_widgets = window.place_slaves()
    for widgets in all_widgets:
        widgets.destroy()
    draw_home_button()


def draw_home_button():
    b = Button(text='Домой', font=('Arial', 18), fg='black', command=draw_menu)
    b.place(x=25, y=500, width=150)


draw_menu():
    if b1 == 1:

window.mainloop()
