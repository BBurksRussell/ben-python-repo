#import random module
import random

#random number generator 1 to 10
rando = random.randint(1, 10)
print(rando)

#color list
colorList = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "magenta", "teal", "burnt orange"]

#print from color list
print("Your randomly selected color from the Color List is "+ colorList[rando-1])

#if 1, color = red; if 2, color = orange etc...
if rando == 1:
    color = "red"
elif rando == 2:
    color = "orange"
elif rando == 3:
    color = "yellow"
elif rando == 4:
    color = "green"
elif rando == 5:
    color = "blue"
elif rando == 6:
    color = "indigo"
elif rando == 7:
    color = "violet"
elif rando == 8:
    color = "magenta"
elif rando == 9:
    color = "teal"
elif rando == 10:
    color = "burnt orange"

#print color
print("Your randomly selected color from the if-then statement is "+ color)
