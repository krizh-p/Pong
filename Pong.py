# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
gameOn = True

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 6
ball.dy = 6

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write("0 : 0", align="center", font=("Courier", 48, "bold"))


# Only Move paddle up if it won't exit the game board
def isValidPaddleMovement(paddle, up=False):
	if (up == False):
		if (paddle.ycor() <= -240):
			return False
		return  True
	else:
		if (paddle.ycor() >= 250):
			return False
		return True
	

# Movement of Paddles
def paddle_a_up():
	if (isValidPaddleMovement(paddle=paddle_a, up=True)):
		y = paddle_a.ycor()
		y += 20
		paddle_a.sety(y)

def paddle_a_down():
	if (isValidPaddleMovement(paddle=paddle_a)):
		y = paddle_a.ycor()
		y -= 20
		paddle_a.sety(y)

def paddle_b_up():
	if (isValidPaddleMovement(paddle=paddle_b, up=True)):
		y = paddle_b.ycor()
		y += 20
		paddle_b.sety(y)

def paddle_b_down():
	if (isValidPaddleMovement(paddle=paddle_b)):
		y = paddle_b.ycor()
		y -= 20
		paddle_b.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while gameOn:
	wn.update()
	
	# Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border checking
	# Top and bottom
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
	
	elif ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
	
	# Left and right
	#Hits Paddle A
	if ball.xcor() > 350:
		score_a += 1
		ball.color("blue")
		pen.clear()
		pen.write("{} : {}".format(score_a, score_b), align="center", font=("Courier", 48, "bold"))
		ball.goto(0, 0)
		ball.dx *= -1

	#Hits Paddle B
	elif ball.xcor() < -350:
		score_b += 1
		ball.color("red")
		pen.clear()
		pen.write("{} : {}".format(score_a, score_b), align="center", font=("Courier", 48, "bold"))
		ball.goto(0, 0)
		ball.dx *= -1

	# Paddle and ball collisions
	if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
		ball.dx *= -1 
	
	elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
		ball.dx *= -1

	#AI for Left Paddle

	# Check for game being finished
	if score_a > 11 or score_b > 11:		
		gameOn = False

while gameOn == False:
	paddle_a.color("black")
	paddle_b.color("black")
	ball.color("black")
	overMessage = turtle.Turtle()
	overMessage.speed(0)
	overMessage.shape("square")
	overMessage.color("white")
	overMessage.penup()
	overMessage.hideturtle()
	overMessage.goto(0, 100)
	overMessage.write("Game Over!", align="center", font=("Courier", 24, "normal"))
	
