import time
from turtle import *

#  ---------------------- Move amount of ball -----------------------#
x_move = 2
y_move = 2
# -------------------------------- UI -------------------------------#
screen = Screen()
screen.tracer(0)
screen.bgcolor("gray")
screen.screensize(canvwidth=400, canvheight=600)
paddle = Turtle("square")
paddle.turtlesize(stretch_len=3, stretch_wid=0.5)
paddle.penup()
paddle.goto(0, -260)

# ---------------------- Create ball---------------#
ball = Turtle("circle")
ball.shapesize(stretch_len=0.5, stretch_wid=0.5)
ball.penup()

# -------------------- create square ---------------#
boxes = []
colors = ["yellow", "orange", "blue", "black"]


def create_box():
    x = -285
    y = 130
    x_add = 80
    y_add = 44
    for j in range(4):
        for i in range(8):
            food = Turtle("square")
            food.shapesize(stretch_wid=2, stretch_len=3.859)
            boxes.append(food)
            food.penup()
            food.color(colors[j])
            food.goto(x, y)
            x += x_add

        y += y_add
        x *= -1
        x +=70


create_box()
print(boxes)
print(len(boxes))
screen.update()


# ------------ Detect collision box with ball---------------#


# ------------------- Move paddle and Ball------------------#
def move_right():
    if paddle.xcor() < 300:
        paddle.setheading(0)
        paddle.forward(40)
    # screen.update()


def move_left():
    if paddle.xcor() > -280:
        paddle.setheading(180)
        paddle.forward(40)
    # screen.update()


def bounce_ball():
    global x_move, y_move
    x = ball.xcor() + x_move
    y = ball.ycor() + y_move
    if x > 320 or x < -320:
        x_move *= -1
    if y > 270:
        y_move *= -1
    if ball.distance(paddle) < 20:
        y_move *= -1
        x_move *= 1

    for boxe in boxes:
        if boxe.distance(ball) < 20:
            y_move *= -1
            boxe.hideturtle()

    ball.goto(x, y)


# --------------------------- Screen Listen Event -----------------------#
screen.listen()
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
# --------------------- Bounce the ball ------------------#
while Turtle:
    screen.update()
    time.sleep(0.01)
    bounce_ball()

screen.mainloop()
