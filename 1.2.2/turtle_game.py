#1.1.2 File
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb


#-----game configuration----
spot_color = "purple"
score=0
font_setup= ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
colors=["red", "green", "blue", "yellow", "purple", "orange"]


#-----initialize turtle-----
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("what is your name?")

#score turtle
score_writer=trtl.Turtle()
score_writer.penup()
box_turtle=trtl.Turtle()
counter =  trtl.Turtle()
counter.penup()


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
    box_turtle.goto(260, 350)
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
    global timer_up
    if timer_up == False:
        change_position()
        meowl.color(rand.choice(colors))

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

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")


#countersetup
def counter_setup():
    counter.pendown()
    counter.forward(-200)
    counter.left(90)
    counter.forward(300)
    counter.right(90)
    counter.hideturtle()

#start countdown and update it each frame
counter.goto(-350, 335)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
# CODE TO ADD
# Add this function to your game code

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global meowl

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, meowl, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, meowl, score)
meowl.onclick(spot_clicked)
scoreBox()

wn = trtl.Screen()
wn.bgcolor("lightgreen")
wn.ontimer(countdown, counter_interval)
wn.mainloop()