import math

#########################################
#A function that takes a list a of numbers and squares each of the numbers in the list. 
#########################################

def square(a):

    for i in range(len(a)):
        a[i] = a[i] ** 2

###############################################################
#A function hat takes a list a of numbers and returns a new list 
# that contains each value in a squared. The original list a should not be modified by your function.
###############################################################

def squared(a):

    return [newList**2 for newList in a]

#########################################
#function lowercase(a) that takes a list a of strings and replaces each string in a with a lowercase version of the string
#########################################

def lowercase(a):

    for i in range(len(a)):
        a[i] = a[i].lower()

#########################################
#function lowercased(a) that takes a list a of strings and returns a new list in that contains a lowercase version of each string in a
#########################################
def lowercased(a):

    return [newList.lower() for newList in a]

#########################################
#Create a new class called Point that represents a point in the Cartesian plane with two coordinates
#########################################

class Point:
    def __init__(self, x, y):
            self.x = x
            self.y = y

    def __str__(self):
        return "({},{})".format(self.x,self.y)

    def __repr__(self):
        return "Point({},{})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and \
               self.y == other.y

#########################################
#A function distance(p, q) that takes two Points p and q and returns the Euclidean distance between p and q.
#########################################

def distance(p,q):

    return math.sqrt(math.pow((q.x - p.x),2) + math.pow((q.y - p.y),2))

#########################################
#A function double(p) that modifies p so that the values of its x- and y-coordinates are doubled.
#########################################

def double(p):
    p.x = p.x * 2
    p.y = p.y * 2

#########################################
#A function doubled(p) that returns a new Point whose x- and y-coordinates are twice those of p
#########################################
def doubled(p):

    return Point(p.x * 2, p.y * 2)
