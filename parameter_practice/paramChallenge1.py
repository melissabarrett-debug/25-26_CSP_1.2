#make 3 methods following details given here
#method 1: name it "tic" and takes 2 parameters "num1" and "num2" and return:
# the value of the 2 parameters when subtracted (ie: num1 - num2)
def tic (num1, num2):
    difference= num1- num2
    return difference
answer=tic(10, 4)
print(answer)


#method 2: name it "tac" and it takes 1 parameter "exp"
#use a loop to multipy the number 5 by itself "exp" times
#return that value
def tac (exp):
    sum=1
    for num in range(exp):
        sum= sum*5
    return sum


#method 3: name it "toe: that takes no parameters. This method should print
#the results of a method call to "tic(3,5)" and "tac(4)" to the console

