import turtle as t

t.title("rainbow!")
t.speed(15)
t.bgcolor("black")
r, g, b = 255, 0, 0
for i in range(255 * 10):
    t.colormode(255)
    if i < 255 // 3:
        g += 3
    elif i < 255 * 2 // 3:
        if r > 0:
            r -= 3
        else:
            r += 3
    elif i < 255:
        b += 3
    elif i < 255 * 4 // 3:
        g += 3
    elif i < 255 * 5 // 3:
        if r > 0:
            r -= 3
        else:
            r += 3
    else:
        b += 3

from turtle import *

tracer(0)
title("rainbow!")
speed(15)
bgcolor("black")
r, g, b = 255, 0, 0
for i in range(255 * 10):
    colormode(255)
    if i < 255 // 3:
        g += 1
    elif i < 255 * 2 // 3:
        if r > 0:
            r -= 1
        else:
            r += 1
    elif i < 255:
        b += 1
    elif i < 255 * 4 // 3:
        g += 1
    elif i < 255 * 5 // 3:
        if r > 0:
            r -= 1
        else:
            r += 1
    else:
        b += 1
    if r > 255:
        r = 0
    elif g > 255:
        g = 0
    elif b > 255:
        b = 0

    t.fd(50 + i)
    t.rt(91)
    t.pencolor(r, g, b)
t.mainloop()

fd(50 + i)
rt(91)
pencolor(r, g, b)
update()
exitonclick()