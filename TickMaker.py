#this is called TickMaker. The goal is to
#take 1 coordinate like this(in feet):
#X = 1353147.7040     Y = 422721.0995     Z = 0.0000
#and generate 4 sets of coordinates that form
#4 corners of a square that is 2500.0 on each side.
#For the coordinates above, the output should be something like this:
#c1 = 1353148.00,422721.0,0
#c2 = 1353148.00,420221.0,0
#c3 = 1350648.00,422721.0,0
#c4 = 1350648.00,420221.0,0

#pull the raw numbers out of the string.
#convert string to float.
#round float
#make 4 corners (c1, c2, c3, c4) by going 2500 ft in each direction from c1.
def ticky(rawCoord):
    interval = 2500
    c1 = [round(float(rawCoord.split(" ")[2])),
          round(float(rawCoord.split(" ")[9])),
          round(float(rawCoord.split(" ")[16]))]
    c2 = [round(float(rawCoord.split(" ")[2])),
          round(float(rawCoord.split(" ")[9])) - interval,
          round(float(rawCoord.split(" ")[16]))]
    c3 = [round(float(rawCoord.split(" ")[2])) - interval,
          round(float(rawCoord.split(" ")[9])),
          round(float(rawCoord.split(" ")[16]))]
    c4 = [round(float(rawCoord.split(" ")[2])) - interval,
          round(float(rawCoord.split(" ")[9])) - interval,
          round(float(rawCoord.split(" ")[16]))]

    return str(c1)
    return str(c2)
    return str(c3)
    return str(c4)
k=input("press close to exit")

