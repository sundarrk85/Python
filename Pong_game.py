# 2 player game
# using turtle programming
# turtle module - beginner game | drawing module
# REFER VIDEO @7.25.00 hrs
# https://youtu.be/BiDOehqG68g
# (x,y)

import turtle
window = turtle.Screen()
window.setup(800,600)   # width, height
window.bgcolor("blue")
window.title("Pong game")
window.tracer(0)           # by default the paddle will be in left side   
# if you run at this point the window will appear and go (like a flash)

# left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)   # I want that paddle to be placed directly in left corner without animation
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)    # width 5 times stretch 
left_paddle.penup()         # it doesn't draw the line while moving
left_paddle.goto(-380,0)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)   # I want that paddle to be placed directly in right corner without animation
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)    # width 5 times stretch 
right_paddle.penup()         # it doesn't draw the line while moving
right_paddle.goto(+380,0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 0.154 # rate of change of movement
ball.dy = 0.154 # rate of change of movement


# moving logic
# press W, S to move left paddle | up, down arrow to move right paddle
# moving paddles
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor() + 20)

def left_paddle_down():
    left_paddle.sety(left_paddle.ycor() - 20)

def right_paddle_up():
    right_paddle.sety(right_paddle.ycor() + 20)

def right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 20)


window.listen()
window.onkeypress(left_paddle_up,'w') 
window.onkeypress(left_paddle_down,'s') 
window.onkeypress(right_paddle_up,'Up') 
window.onkeypress(right_paddle_down,'Down') 




# to display the window 
while True:
    window.update()
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball - collision on wall 
    # top wall
    if ball.ycor() > 290:
        ball.sety(290) 
        ball.dy *= -1           # opposite side
    
    # bottom wall
    if ball.ycor() > -290:
        ball.sety(-290) 
        ball.dy *= -1           # opposite side
        

