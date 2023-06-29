import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()

# создаем рабочую область
frame = tkinter.Frame(window)
frame.grid()


#Добавим изображение
canvas = tkinter.Canvas(window, height=400, width=700)
image = Image.open("1.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw',image=photo)
canvas.grid(row=2,column=1)
window.mainloop()