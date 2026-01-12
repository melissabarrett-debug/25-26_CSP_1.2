import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25 #horizontal offest letters
apple_letter_y_offset = -50 #vertical offest letters
current_letter="a" #our current letter
screen_width= 400 #width of screen
screen_height= 400 #height of screen

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
letters=["a", "b", "c", "d", "e" "f", "g", "h" "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]

def reset_apple(active_apple):
    #generate a random number -> pop that index
    #the letter we pop, becomes the letter on the apple
    global current_letter
    #how many letters are left
    length_of_list= len(letters)
    # if we aren't out
    if (length_of_list != 0):
        #pick a random numer
        index=rand.randint(0, length_of_list)
        #set the random letter to our current letter
        current_letter= letters.pop(index)
        #Goto:x and y -> randomize each
        #active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2), rand.randint(-(screen_height) / 2, (screen_height) / 2))
        active_apple.goto(200, 200)
        draw_apple(active_apple, current_letter)

wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, current_letter):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  draw_letter(current_letter, active_apple)
  wn.update()

def drop_apple():
    wn.tracer(True)
    apple.goto(apple.xcor(), ground_height)
    apple.clear()
    apple.hideturtle()
    wn.tracer(False)
    apple.hideturtle()
    reset_apple(apple)

def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 74, "bold"))
  active_apple.setpos(remember_position)

def check_apple_a():
    if (current_letter == "a"):
        drop_apple()

#change the letters for these
def check_apple_a():
    if (current_letter == "a"):
        drop_apple()

def check_apple_a():
    if (current_letter == "a"):
        drop_apple()

def check_apple_a():
    if (current_letter == "a"):
        drop_apple()

def check_apple_a():
    if (current_letter == "a"):
        drop_apple()





draw_apple(apple, current_letter)

wn.onkeypress(check_apple_a, "a")


#   a123_apple_and_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty.

#TODO Create a function that draws a new letter from the letter list.

#TODO Create a function that takes a turtle (apple) as its parameter
# and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
#for i in range(0, number_of_apples):


#TODO Create a function that takes a letter as its parameter, retrieve a
# random turtle (apple) and causes the turtle (apple) to drop from the tree and the letter
# to disappear. Call the apple resetting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop an apple at random.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.
wn.onkeypress(drop_apple, "a")



wn.listen()
trtl.mainloop()