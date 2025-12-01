#import turtle
import turtle as trtl

#make a turtle
james = trtl.Turtle()




def drawSquare():
    for sides in range(4):
        james.forward(30)
        james.right(90)


drawSquare()
james.forward(60)
drawSquare()

wn = trtl.Screen()
wn.mainloop()

#goal: to draw squares with a turtle