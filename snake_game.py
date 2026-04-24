import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0

# Screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("blue")
s.setup(width=600, height=600)
s.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.penup()
food.goto(0,100)

# Snake body
bodies = []

# Scoreboard
sb = turtle.Turtle()
sb.speed(0)
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(-250,260)
sb.write("Score: 0 | High Score: 0", align="left", font=("Arial",14,"normal"))

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard control
s.listen()
s.onkey(go_up,"Up")
s.onkey(go_down,"Down")
s.onkey(go_left,"Left")
s.onkey(go_right,"Right")

# Game loop
while True:

    s.update()

    # Border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:

        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        for body in bodies:
            body.goto(1000,1000)

        bodies.clear()

        score = 0
        delay = 0.1

        sb.clear()
        sb.write(f"Score: {score} | High Score: {high_score}",
                 align="left",font=("Arial",14,"normal"))

    # Food collision
    if head.distance(food) < 20:

        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        # Add body
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("red")
        body.penup()
        bodies.append(body)

        score += 10

        if score > high_score:
            high_score = score

        sb.clear()
        sb.write(f"Score: {score} | High Score: {high_score}",
                 align="left",font=("Arial",14,"normal"))

    # Move body
    for i in range(len(bodies)-1,0,-1):

        x = bodies[i-1].xcor()
        y = bodies[i-1].ycor()
        bodies[i].goto(x,y)

    if len(bodies) > 0:
        bodies[0].goto(head.xcor(),head.ycor())

    move()

    time.sleep(delay)







