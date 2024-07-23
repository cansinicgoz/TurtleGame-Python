import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("dark blue")
drawing_board.title("Turtle Game")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(150)

def rotate_angle_right():
    turtle_instance.right(50)


def rotate_angle_left():
    turtle_instance.left(50)


def clear_screen():
    turtle_instance.clear()

def retrun_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angle_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=retrun_home,key="h")
drawing_board.onkey(fun=turtle_pen_down,key="a")
drawing_board.onkey(fun=turtle_pen_up,key="z")
drawing_board.mainloop()