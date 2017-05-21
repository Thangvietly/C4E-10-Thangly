from turtle import*
color("yellow","yellow")
def draw_star(x,y,length):
    
#x,y: location of the star
    penup()
    goto(x,y)
    pendown()
    for _ in range(5):
        fd(length)
        rt(144)

draw_star(20,30,100)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

# random.randint is one of Random function.
# If we wanted a random interger, we can use "randint funtion".
#It accepts two parameters: a lowest and a highest number
