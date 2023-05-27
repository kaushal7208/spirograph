import turtle as t
import random
kaash = t.Turtle()
t.colormode(255)
kaash.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    rgb = (r,g,b)
    return rgb


for i in range(100):
    n = 10
   
    kaash.circle(100)
    kaash.left(n -5)
    kaash.color(random_color())
    # kaash.fd(360)
    
    n+=10











screen = t.Screen()
screen.exitonclick()