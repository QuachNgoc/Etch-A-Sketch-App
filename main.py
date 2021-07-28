from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.width(5)


def move_fd():
    tim.forward(10)


def move_bd():
    tim.forward(-10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


screen.listen()
# Set focus on TurtleScreen (in order to collect key-events).
# Dummy arguments are provided in order to be able to pass listen() to the onclick method.
screen.onkeypress(move_fd, "Up")
screen.onkeypress(move_bd, "Down" )
screen.onkeypress(clear, "c")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")

screen.exitonclick()
