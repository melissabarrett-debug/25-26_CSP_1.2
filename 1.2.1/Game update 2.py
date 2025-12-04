#-----import statements-----
import turtle as trtl
import random as rand



#-----game configuration----
spot_color = "purple"
score=0
score_writer=trtl.Turtle()
#-----initialize turtle-----
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()

#-----game functions--------
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
    global score
    score+=1
    print(score)
#-----events----------------
meowl.onclick(spot_clicked)



wn = trtl.Screen()
wn.mainloop()