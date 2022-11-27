import turtle
import random
import timeit

screen = turtle.Screen()
screen.setup(800,800)

guess = screen.textinput(prompt = "du doan con rua nao chien thang?", 
                     title = "nhap vao mau con rua lua chon (red, brown, blue, green, orange, pink)")

print("ban du doan con thang cuoc la con rua mau:",guess)

colors = ["red","brown", "blue","green","orange","pink"]

y_position = [0,-30,30,-60,60,90]

turtle_speed = [5,10,15,20,25,30]

all_turtles = []

turtle.hideturtle()

turtle.speed(0)

run = True

# ve dich
vd = turtle.Turtle()
vd.penup()
vd.pensize(5)
vd.pencolor("red")
vd.goto(250,-180)
vd.left(90)
vd.pendown()
vd.forward(400)
vd.hideturtle()

# ve duong dua
dd = turtle.Turtle()
dd.penup()
dd.hideturtle()
dd.goto(-250,210)
dd.left(90)
for i in range(-250,250,25):
    for j in range(-100,130,30):
        dd.penup()
        dd.goto(i,j)
        dd.pendown()
        dd.forward(15)
        
# ve truc so
for i in range(21):
    ts = turtle.Turtle()
    ts.speed(0)
    ts.hideturtle()
    ts.penup()
    ts.goto(-250 + i*25, 135)
    ts.write(i)
    
    ts.penup()
    ts.goto(-250 + i*25, -120)
    ts.write(i)
        
# thiet lap vi tri ban dau cua rua, luu mau cac con rua vao list

for rua in range(6):
    t = turtle.Turtle(shape = "turtle")
    t.penup()
    t.goto(-250,y_position[rua])
    t.color(colors[rua])
    all_turtles.append(t)
    
# ham di chuyen cac con rua

winner_turtle = -1

def random_walk(ruas):
    global run
    global winner_turtle
    j = 0
    for i in ruas:
        i.forward(random.choice(turtle_speed))
        if i.xcor() >= 250:
            winner_turtle = j
            run = False
        j += 1

start_time = timeit.default_timer()
        
while run:
    random_walk(all_turtles)

stop_time = timeit.default_timer()

print("thoi gian chay cua con rua nhanh nhat la: ",stop_time - start_time)
    
if guess == colors[winner_turtle]:
    print("con rua chien thang la rua mau:",colors[winner_turtle], '\n',
         "chuc mung ban da du doan dung !!!")
else:
    print("Rat tiec, con rua chien thang la rua mau:",colors[winner_turtle], '\n',
         "chuc ban may man lan sau !")

screen.exitonclick()