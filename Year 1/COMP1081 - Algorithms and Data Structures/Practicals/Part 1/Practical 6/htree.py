#adspractical6kochcurve.py
#algorithms and data structures practical week 6
#matthew johnson 9 november 2012
#last revised 10 november 2013

#####################################################

import tkinter
import math


def koch(mp, length, depth):
    """draw a koch curve between start and finish of stated recursion depth"""
    [L, R, LUP, LDN, RUP, RDN] = calculate_points(mp,length)
    if depth == 0:
        connect_points([LUP,LDN])
        connect_points([RUP,RDN])
        connect_points([L,R])
    else:
        koch(LUP,length/2, depth - 1)
        koch(LDN, length/2, depth - 1)
        koch(RUP, length/2, depth - 1)
        koch(RDN, length/2, depth - 1)

#runs when start button is pressed
def start():
    koch(*initial_conditions())
    

def initial_conditions():
    # return coordinate(100.0,180.0), 50, int(recursiondepth.get())
    return coordinate(100.0, 180.0), 100, int(recursiondepth.get())

def calculate_points(mp, length):
    L=mp-coordinate((length/2),0)
    R=mp+coordinate((length/2),0)
    LUP=L+coordinate(0,(length/2))
    LDN=L-coordinate(0,(length/2))
    RUP=R+coordinate(0,(length/2))
    RDN=R-coordinate(0,(length/2))


    return [L,R,LUP,LDN,RUP,RDN]

def connect_points(points):
    """draws lines to connect a list of points together"""
    for i in range(len(points) - 1):
        draw_line(points[i], points[i+1])

def draw_line(u, v):
    """draws a straight line between two coordinates u and v"""
    canvas.create_line(u.x, u.y, v.x, v.y)

def draw_triangle(left, right, bottom, colour="#f62817"):
    """draw triangle given coordinates of corners and colour for fill"""
    canvas.create_polygon(left.x, left.y, right.x, right.y, bottom.x, bottom.y, fill=colour)



def square(midpoint, length, colour):
    """draws a square of given midpoint length and colour"""
    offset = coordinate(length/2, length/2)
    bottomleft = midpoint - offset
    topright = midpoint + offset
    canvas.create_rectangle(bottomleft.x, bottomleft.y, topright.x, topright.y, fill=colour)


class coordinate(object):
    """creates a class for coordinates in the x-y plane
    that can be added and multiplied by constants"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return coordinate(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return coordinate(self.x - other.x, self.y - other.y)
    def __mul__(self, const):
        return coordinate(const * self.x, const * self.y)
    def perpendicular(self):
        """rotate 90 degrees anticlockwise"""
        return coordinate(self.y, self.x * (-1))

def midpoint(c1, c2):
    """finds the midpoint of two coordinates"""
    return(coordinate((c1.x+c2.x)/2, (c1.y+c2.y)/2))


   
#####################################################

#clears the canvas when clear button is pressed
def clear():
    canvas.delete("all")
    
#set up window with buttons, labels etc
window = tkinter.Tk()
window.title("ADS Practical 6: Koch curve")
clear_button = tkinter.Button(window, text = "Clear", command = clear)
start = tkinter.Button(window, text="Start", command=start)
recursiondepth=tkinter.StringVar()
defaultrecursion = 0 #default depth of recursion
recursiondepth.set(defaultrecursion)
recLabel=tkinter.Label(window, width="17")
recLabel.configure(text="    Depth of recursion =   ")
recentry=tkinter.Entry(window, width="2", textvariable=recursiondepth)
canvas = tkinter.Canvas(window, width=620, height=600)
canvas.pack(side="top")
start.pack(side="right")
clear_button.pack(side = "right")
recLabel.pack(side="left")
recentry.pack(side="left")

# start event loop
window.mainloop()
