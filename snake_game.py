import turtle
import random
import time
 
# ---------------- Game settings ----------------
delay = 0.1        # speed of the game (lower = faster)
score = 0
high_score = 0
 
# ---------------- Screen setup ----------------
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("blue")
s.setup(width=600, height=600)
s.tracer(0)  # turns off automatic screen updates, we update manually for smoother animation
 
# ---------------- Snake head ----------------
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"  # snake doesn't move until a key is pressed
 
# ---------------- Food ----------------
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.penup()
food.goto(0, 100)
 
# ---------------- Snake body segments ----------------
bodies = []  # will hold each body segment turtle
 
# ---------------- Scoreboard ----------------
sb = turtle.Turtle()
sb.speed(0)
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(-250, 260)
sb.write("Score: 0 | High Score: 0", align="left", font=("Arial", 14, "normal"))
 
 
# ---------------- Movement functions ----------------
def go_up():
    # prevent snake from reversing directly into itself
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
    # moves the head one step in whatever direction it's currently facing
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
 
 
# ---------------- Keyboard bindings ----------------
s.listen()
s.onkey(go_up, "Up")
s.onkey(go_down, "Down")
s.onkey(go_left, "Left")
s.onkey(go_right, "Right")
 
 
# ---------------- Main game loop ----------------
# Wrapped in try/except so closing the window doesn't crash with a traceback.
# turtle.Terminator is raised internally the moment you close the window
# while the loop is still calling s.update() (or any drawing call) —
# there's simply nowhere left to draw. Catching it lets us exit cleanly.
try:
    while True:
 
        s.update()
 
        # ---- Border collision: reset game if snake hits the wall ----
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
 
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
 
            # send all body segments off screen and clear the list
            for body in bodies:
                body.goto(1000, 1000)
            bodies.clear()
 
            score = 0
            delay = 0.1
 
            sb.clear()
            sb.write(f"Score: {score} | High Score: {high_score}",
                     align="left", font=("Arial", 14, "normal"))
 
        #Food collision: grow snake and increase score
        if head.distance(food) < 20:
 
            # move food to a new random position
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x, y)
 
            # add a new body segment
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
                     align="left", font=("Arial", 14, "normal"))
 
        # ---- Move body segments (each one follows the one in front of it) ----
        for i in range(len(bodies) - 1, 0, -1):
            x = bodies[i - 1].xcor()
            y = bodies[i - 1].ycor()
            bodies[i].goto(x, y)
 
        # first body segment follows the head
        if len(bodies) > 0:
            bodies[0].goto(head.xcor(), head.ycor())
 
        move()
 
        time.sleep(delay)
 
except turtle.Terminator:
    # Raised when the turtle window is closed mid-loop.
    # We just exit quietly instead of printing a traceback.
    print("Game window closed. Exiting cleanly.")
