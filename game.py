import random
import turtle

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)

x = random.randint(1, 100)

print(x)

turtle.speed(0)

turtle.circle(30)

#вертикальная
draw_line(-160, -100, -160, 80)
#горизонтальная
draw_line(-160, 80, -80, 80)

draw_line(-160, 40, -120, 80)
draw_line(-100, 80, -100, 40)


gotoxy(-100, 0)
turtle.circle(20)

draw_line(-100, 0, -100, -50)

draw_line(-100, -10, -120, -50)

draw_line(-160, -10, -120, -20)
draw_line(-100, -10, -80, -20)

draw_line(-100, -50, -120, -60)
draw_line(-100, -50, -80, -60)
input('Нажмите любую клавишу')
