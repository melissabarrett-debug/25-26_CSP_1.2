#-----import statements-----
import turtle as trtl
import random as rand



#-----game configuration----
spot_color = "purple"
score=0
font_setup= ("Arial", 20, "normal")

#-----initialize turtle-----
score_writer=trtl.Turtle()
score_writer.penup()
box_turtle=trtl.Turtle()

#shape turtle
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
box_turtle.penup()
meowl.penup()

#-----game functions--------
#draw the box for the score
def scoreBox():
    box_turtle.goto(375, 325)
    box_turtle.pendown()
    #draw box
    for sides in range(2):
        box_turtle.forward(100)
        box_turtle.left(90)
        box_turtle.forward(50)
        box_turtle.left(90)
    #place score box
    score_writer.penup()
    score_writer.goto(300, 350)
    #hide turtles
    score_writer.hideturtle()
    box_turtle.hideturtle()
# Get a score boost, move the turtle randomly
def spot_clicked(x, y):
    change_position()

def change_position():
    # Move the turtle to a random location
    newX = rand.randint(-300, 300)
    newY = rand.randint(-300, 300)
    meowl.goto(newX, newY)
    update_score()

def update_score():
    #include global score
    global score
    #increment the score by 1
    score+=1
    score_writer.clear()
    #print the current score
    score_writer.write(score, font=font_setup)

#-----events----------------
meowl.onclick(spot_clicked)


scoreBox()
wn = trtl.Screen()
wn.mainloop()