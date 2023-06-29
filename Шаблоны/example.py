import tkinter as tk
import requests
from bs4 import BeautifulSoup
import random


def draw_menu():
    all_widgets = win.place_slaves()  # Получаем список всех виджетов
    for i in all_widgets:
        i.destroy()
        label_title = tk.Label(win, text="Что вы хотите сделать?", font=("arial", 24), fg="white", bg="orange")
        label_title.place(width=700, height=50)
        btn1 = tk.Button(win, text="Узнать факт", font=("arial", 18), fg="black", bg="#D6D6D6",command=get_interesting_fact)
        btn1.place(x=25, y=75, width=300)
        btn2 = tk.Button(win, text="Посмотреть на котиков", font=("arial", 18), fg="black", bg="#D6D6D6", command=get_cat)
        btn2.place(x=375, y=75, width=300)


def clear():
    all_widgets = win.place_slaves()  # Получаем список всех виджетов


for i in all_widgets:
    i.destroy()
    home_button()


def home_button():
    home_btn = tk.Button(win, text="Домой", font=("arial", 24), command=draw_menu)
    home_btn.place(x=25, y=500, width=150)


def get_cat():
    clear()
    response = requests.get("https://bigpicture.ru/100-luchshix-fotografij-koshek-vsex-vremen-i-narodov/?ysclid=lar6w7h54y805117860")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    allcats = html.find_all("figure", class_="wp-caption")
    cats = []
    for i in allcats:
        cats.append(i.find("img").get("src"))
        print(cats)

win = tk.Tk()
win.geometry("700x600")
draw_menu()

win.mainloop()
