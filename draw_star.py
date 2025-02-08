import turtle

def draw_star(color, size):
    sprite.color(color)
    sprite.pensize(3)
    sprite.begin_fill()
    for i in range(12):
        sprite.forward(size)
        sprite.right(150)
    sprite.end_fill()

turtle.mode( "logo")
stage = turtle.Screen()
sprite = turtle.Turtle()
sprite.setheading( 90)

draw_star("red",180)

stage.mainloop()