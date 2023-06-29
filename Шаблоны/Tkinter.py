from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')

canvas = Canvas(ws, width=500, height=500)
canvas.pack()
img = PhotoImage(file='venv//1.jpg')
canvas.create_image(10, 10, anchor=NW, image=img)
ws.mainloop()
'''import tkinter as tk
from PIL import Image, ImageFilter, ImageTk

try:
    original = Image.open("озеро.jpg")
except FileNotFoundError:
    print("Файл не найден")

blurred = original.filter(ImageFilter.BLUR)
# открываем оригинал и размытое изображение
original.show()
blurred.show()
# сохраняем изображение
blurred.save("blurred.png")
size = (500, 600)
saved = "озеро.jpg"
img = Image.open("озеро.jpg")
img.thumbnail(size)
img.save(saved)
img.show()
# указываем фиксированный размер стороны
image_path='озеро.jpg'
fixed_width = 600
img = Image.open(image_path)
# получаем процентное соотношение
# старой и новой ширины
width_percent = (fixed_width / float(img.size[0]))
# на основе предыдущего значения
# вычисляем новую высоту
height_size = int((float(img.size[0]) * float(width_percent)))
# меняем размер на полученные значения
new_image = img.resize((fixed_width, height_size))
new_image.show()'''
'''def show_image(path):
    root = tk.Tk()
    img = Image.open(path)
    width = 600
    ratio = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(ratio)))
    imag = img.resize((width, height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(imag)
    panel = tk.Label(root, image=image)
    panel.pack(side="top", fill="both", expand="no")
    #tk.Button(root, text='Quit', command=root.quit).place(x=250, y=250)
    root.mainloop()

show_image('озеро.jpg')

root = tk.Tk()
img = Image.open('озеро.jpg')
width = 600
ratio = (width / float(img.size[0]))
height = int((float(img.size[1]) * float(ratio)))
imag = img.resize((width, height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(imag)
panel = tk.Label(root, image=image)
panel.pack(side="top", fill="both", expand="no")
#tk.Button(root, text='Quit', command=root.quit).place(x=250, y=250)
root.mainloop()'''

