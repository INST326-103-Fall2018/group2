import turtle
import csv



print("Let's play Pong! First to 5 points wins!")



wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Assigns names to players
p1 = wn.textinput("Player Names", "Name of first player:")
p2 = wn.textinput("Player Names", "Name of secone player:")

# Score
score_a = 0
score_b = 0

#Creating paddles
#paddle a
paddle_a = turtle.Turtle() #creating paddleA turtle object
paddle_a.speed(0) #doesn't move by itself
paddle_a.shape("square") #shape
paddle_a.color("white") #color
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #size
paddle_a.penup()
paddle_a.goto(-350, 0) #sets starting coordinate

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#sets how fast the ball goes
ball.dx = 3 #change in x speed
ball.dy = 3 #change in y speed

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"{p1}: 0  {p2}: 0",
            align="center",font=("Menlo", 24, "normal")) #sets the default score

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bouncing the ball off edges
    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses y direction

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #reverses y direction

    # Left and right and scoring
    if ball.xcor() > 350:
        score_a += 1 #increments score
        pen.clear() #clears original score
        pen.write(f"{p1}: {score_a}  {p2}: {score_b}",
                align="center", font=("Menlo", 24, "normal")) #adds score
        ball.goto(0, 0)
        ball.dx *= -1 #reverses x direction when scored

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write(f"{p1}: {score_a}  {p2}: {score_b}",
                align="center", font=("Menlo", 24, "normal")) #adds score
        ball.goto(0, 0)
        ball.dx *= -1 #reverses x direction when scored

    # Paddle and ball bouncing
    #if the ball passes the x cor of the paddle AND is between the y coords of the paddle, bounce
    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    #Determines winner and adds instance of win
    if score_a == 5 or score_b ==5:
        p1wins = 0
        p2wins = 0

        if score_a > score_b:
            p1wins += 1
        elif score_b > score_a:
            p2wins += 1

        scores_dict = {'game': 'Pong', f'{p1} wins': p1wins, f'{p2} wins': p2wins}

        with open('scores.csv', 'a') as f:
            w = csv.DictWriter(f, scores_dict.keys())
            w.writeheader()
            w.writerow(scores_dict)
        turtle.bye()
