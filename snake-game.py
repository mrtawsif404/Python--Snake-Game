import turtle
import time
import random

# Game window setup
wn = turtle.Screen()
wn.title("Snake Game - Designed by Tawsif")
wn.bgcolor("#0b3d0b") # Deep green background (Grass field look)
wn.setup(width=600, height=600)
wn.tracer(0)

# Draw Border Arena (White glowing border)
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.goto(-290, 290)
border_pen.pendown()
border_pen.pensize(3)
for _ in range(4):
    border_pen.forward(580)
    border_pen.right(90)
border_pen.hideturtle()

# Snake head (Realistic circle head with neon cyan color)
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#00ffcc") 
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food (Vibrant red glowing apple)
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#ff3333") 
food.penup()
food.goto(0, 100)

segments = []

# Score display
score = 0
high_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 18, "bold"))

# Functions for movement
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

# Keyboard bindings (W, A, S, D and Arrow Keys)
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check collision with border
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        
        score = 0
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 18, "bold"))

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#00cc66") # Bright green body
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 18, "bold"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            
            score = 0
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 18, "bold"))

    time.sleep(0.09) 