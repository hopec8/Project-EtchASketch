import turtle as t

cursor = t.Turtle()
screen = t.Screen()

def move_forward():
    cursor.forward(50)

def move_backward():
    cursor.backward(50)

def turn_right():
    cursor.right(45)

def turn_left():
    cursor.left(45)

def clear():
    t.clear()
    t.home()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear, "c")

screen.exitonclick()