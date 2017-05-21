from turtle import*

def draw_square(length, col):
    color(col)
    for _ in range(4):
        fd(length)
        left(90)
        
draw_square(100,"red")

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
