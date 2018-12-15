##!/usr/bin/env python3
#Name: Matthew Ye
#Assignment Final Project

# PONG STYLE GAME

import turtle
import csv
import sys


def main():
    # Score
    score_a = 0
    score_b = 0

    print("Let's play Pong! First to 5 points wins!\nType 'exit' to end the game")

    #Creating window/screen
    wn = turtle.Screen() #creating window turtle object
    wn.title("Pong") #sets title
    wn.bgcolor("black") #set background color to black
    wn.setup(width=800, height=600) #set screen/window dimensions
    wn.tracer(0)


    #Assigns names to players
    p1 = wn.textinput("Player Names", "Name of first player:")
    p2 = wn.textinput("Player Names", "Name of second player:")


    #Creating paddles
    #Paddle A
    paddle_a = turtle.Turtle() #creating paddle turtle object
    paddle_a.speed(0) #make it stationary
    paddle_a.shape("square") #shape
    paddle_a.color("white") #color
    paddle_a.shapesize(stretch_wid=5,stretch_len=1) #size
    paddle_a.penup()
    paddle_a.goto(-350, 0) #sets starting coordinate

    #Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    #making the ball
    ball = turtle.Turtle() #creates ball object
    ball.speed(0) #make it stationary
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0) #set starting location

    #sets ball speed
    ball.dx = 3 #change in x speed
    ball.dy = 3 #change in y speed

    #creating the score
    pen = turtle.Turtle() #creates pen object
    pen.speed(0) #make it stationary
    pen.shape("square") #make it square
    pen.color("white") #make it white
    pen.penup()
    pen.hideturtle() #hide the object
    pen.goto(0, 260) #sets location
    pen.write(f"{p1}: 0  {p2}: 0",
                align="center",font=("Menlo", 24, "normal")) #sets the default score

    #moving the paddles
    def paddle_a_up():
        y = paddle_a.ycor() #sets y equal to paddle A's Y coordinate
        y += 25 #increments paddle location by 25
        paddle_a.sety(y) #moves the paddle's y coord to new location

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

    #Keyboard controls
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    #----MAIN GAME LOOP----#
    while True:
        wn.update() #update game window

        #moving the ball
        ball.setx(ball.xcor() + ball.dx) #sets ball x coord to current + change in x
        ball.sety(ball.ycor() + ball.dy) #sets ball y coord to current + change in y

        #Bouncing the ball off edges
        #Top and bottom edges
        if ball.ycor() > 290: #if the ball goes higher than the window edge
            ball.sety(290)
            ball.dy *= -1 #reverses y direction (make it go down)

        elif ball.ycor() < -290: #if the ball goes lower than the window edge
            ball.sety(-290)
            ball.dy *= -1 #reverses y direction (make it go up)

        #Left and right edges (and scoring)
        if ball.xcor() > 350: #if the ball goes past right edge
            score_a += 1 #increments score
            pen.clear() #clears original score
            pen.write(f"{p1}: {score_a}  {p2}: {score_b}",
                    align="center", font=("Menlo", 24, "normal")) #writes new score
            ball.goto(0, 0) #resets the ball
            ball.dx *= -1 #reverses ball direction when scored

        elif ball.xcor() < -350: #if the ball goes past the left edge
            score_b += 1 #increments score
            pen.clear() #clears original score
            pen.write(f"{p1}: {score_a}  {p2}: {score_b}",
                    align="center", font=("Menlo", 24, "normal")) #writes new score
            ball.goto(0, 0) #resets the ball
            ball.dx *= -1 #reverses ball direction when scored

        #Paddle and ball bouncing
        #if the ball passes the x cor of the paddle AND is between the y coords of the paddle, bounce
        if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1 #bounce aka reverse ball left/right direction

        elif ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1



        #Determines winner and adds instance of win then closes game
        winnerscore = None

        if score_a == 5 or score_b == 5:
            p1wins = 0
            p2wins = 0

            if score_a > score_b:
                p1wins += 1
                winnerscore = score_a
            elif score_b > score_a:
                p2wins += 1
                winnerscore = score_b
            break
        elif sys.argv[0] == 'exit':
            print('Thanks for playing, goodbye!')
            break


    print('q', winnerscore)

if __name__ == '__main__':
    main()
