from tkinter import *
from random import randint

window = Tk()
window.geometry('600x600')
canvas = Canvas(window, width=600, height=600)
canvas.pack()


class Fire:
    image = PhotoImage(file='fire.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Soil):
            return Clay
        elif isinstance(other, Water):
            return Steam


class Soil:
    image = PhotoImage(file='soil.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay
        elif  isinstance(other, Water):
            return Plant
        elif isinstance(other, Air):
            return Dust


class Air:
    image = PhotoImage(file='fresh-air.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Soil):
            return Clay
        elif isinstance(other, Soil):
            return Dust


class Water:
    image = PhotoImage(file='water-drop.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Soil):
            return Plant
        elif isinstance(other, Fire):
            return Steam


class Plant:
    image = PhotoImage(file='plant.png').subsample(4, 4)


class Clay:
    image = PhotoImage(file='clay-crafting.png').subsample(4, 4)


class Dust:
    image = PhotoImage(file='dust.png').subsample(4, 4)


class Steam:
    image = PhotoImage(file='steam.png').subsample(4, 4)


def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    print(images_id)
    if len(images_id) == 2:
        elem_1 = elements[images_id[0] - 1]
        elem_2 = elements[images_id[1] - 1]
        new_elem = elem_2 + elem_1
        if new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)
    canvas.coords(images_id, event.x, event.y)


elements = [
    Fire(),
    Air(),
    Water(),
    Soil(),
]

for elem in elements:
    canvas.create_image(randint(50, 350), randint(50, 350), image=elem.image)

window.bind('<B1-Motion>', move)

window.mainloop()