import random
import turtle as t
t.bgcolor('yellow')
catterpillar = t.Turtle()
catterpillar.shape('square')
catterpillar.color('red')
catterpillar.speed(0)
catterpillar.penup()
catterpillar.hideturtle()
catterpillar2 = t.Turtle()
catterpillar2.color('blue')
catterpillar2.shape('square')
catterpillar2.penup()
catterpillar2.speed(0)
catterpillar2.hideturtle()
leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)
game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start!', align='center',\
                  font=('Arial', 16, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.hideturtle()
score_turtle.speed(0)
def outside_window(catterpillar):
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottem_wall = -t.window_height() / 2
    (x, y) = catterpillar.pos()
    outside = \
            x< left_wall or\
            x> right_wall or\
            y< bottem_wall or\
            y> top_wall
    return outside

def game_over():
    catterpillar.color('yellow')
    catterpillar2.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align='center', font=('Arial', 30, 'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right',\
                       font=('Arial', 40, 'bold'))
def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st()          
def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text_turtle.clear()
    catterpillar_speed = 2
    catterpillar_length = 3
    catterpillar.shapesize(1, catterpillar_length, 1)
    catterpillar.showturtle()
    catterpillar2.shapesize(1, catterpillar_length, 1)
    catterpillar2.setheading(180)
    catterpillar2.showturtle()
    display_score(score)
    place_leaf()

    while True:
        catterpillar.forward(catterpillar_speed)
        catterpillar2.forward(catterpillar_speed)
        if catterpillar.distance(leaf) < 20 or leaf.distance(catterpillar2) < 20:
            place_leaf()
            catterpillar_length = catterpillar_length + 1
            catterpillar.shapesize(1, catterpillar_length, 1)
            catterpillar2.shapesize(1, catterpillar_length, 1)
            catterpillar_speed = catterpillar_speed + 1
            score = score + 1
            display_score(score)
        if outside_window(catterpillar) or outside_window(catterpillar2):
            game_over()
            break
def move_up():
    if catterpillar.heading() == 0 or catterpillar.heading() == 180:
        catterpillar.setheading(90)

def move_down():
    if catterpillar.heading() == 0 or catterpillar.heading() == 180:
        catterpillar.setheading(270)
        
def move_left():
    if catterpillar.heading() ==90 or catterpillar.heading() == 270:
        catterpillar.setheading(180)

def move_right():
    if catterpillar.heading() == 90 or catterpillar.heading() == 270:
        catterpillar.setheading(0)
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
def catterpillar2_move_up():
    if catterpillar2.heading() == 0 or catterpillar2.heading() == 180:
        catterpillar2.setheading(90)
        
def catterpillar2_move_down():
    if catterpillar2.heading() == 0 or catterpillar2.heading() == 180:
        catterpillar2.setheading(270)

def catterpillar2_move_left():
    if catterpillar2.heading() == 90 or catterpillar2.heading() == 270:
        catterpillar2.setheading(180)

def catterpillar2_move_right():
    if catterpillar2.heading() == 90 or catterpillar2.heading() == 270:
        catterpillar2.setheading(0)

t.onkey(catterpillar2_move_up, 'w')
t.onkey(catterpillar2_move_right, 'd')
t.onkey(catterpillar2_move_down, 's')
t.onkey(catterpillar2_move_left, 'a')
t.listen()
t.mainloop()
