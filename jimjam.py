def jimmy(x):
  for foo in x:
    if foo % 2 == 0:
      print "jam"
    else:
      print "jim"

##Given a string, return the count of the number of times that a substring
##length 2 appears in the string and also as the last 2 chars of the string,
##so "hixxxhi" yields 1 (we won't count the end substring). 
##
##last2('hixxhi') → 1
##last2('xaxxaxaxx') → 1
##last2('axxxaaxx') → 2
#get rid of the strings that are too small
def last2(str):
  if len(str)<2:
    return 0
#determine what the last 2 letters are and set those to a variable.  
  last2 = str[len(str)-2:]
#you will loop through the string and count the number of times last2 is in it
#so start the count at 0 before the loop begins
  count = 0
#now the loop is beginning. In a range equal to the length of the str, minus
#the last 2 chars, compare each of the chars, plus the next one (x+2)
# to the value of last 2. if its the same, increment count by 1.   
  for x in range(len(str)-2):
    sub = str[x:x+2]
    if sub == last2:
      count = count + 1
  return count
  
#this funcion getdistance will calculate the distance between to x,y coordinates
# on a 2D plane.
def getdistance(a, b):
        #the math library contains abs() and sqrt()
	import math
        #the xdist and ydist variables will be float-converted numbers equal to the
	#distance between the two x values and y values
	xdist = float(abs(a[0] - b[0]))
        #printing values to test
	print xdist
	ydist = float(abs(a[1] - b[1]))
	print ydist
	return math.sqrt((xdist*xdist) + (ydist*ydist))
