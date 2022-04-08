#https://adventofcode.com/2015/day/3
#TUSHAR MAHARANA
#tusharhero.mit-license.org
#instructions:
'''
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
'''

#We will use a cartesian system to do this.

def mov(c,m):#takes a coordinate as a list and moves the point as per the rules i'e ^ up , v down , > right , < left
    x = c[0]#taking the values of x and y respectively
    y = c[1]
    if m == "^":#manipulating the x and y according to the symbol
        y = y + 1
    if m =="v":
        y = y - 1
    if m == ">":
        x = x + 1
    if m == "<":
        x = x - 1
    c = [x,y]#creating a list 
    return c

def movstr(c,mstr):#creates a list of all positions after each move.
    l = len(mstr)
    a = 0
    cl = []
    while a < l:
        cl.append(c)
        c = mov(c,mstr[a])
        a = a + 1
    return cl

def isitinlist(l,i):#checks if an item exists in the list takes the list and item as input
    le = len(l)
    a = 0
    while a < le:
        if i == l[a]:
            return 1
        a = a + 1
    return 0

def getuniq(c,mstr):
    mvstr = movstr(c,mstr)
    l = len(mvstr)
    a = 0
    clq = []
    while a < l:
        if isitinlist(mvstr, mvstr[a]) == 1:
            clq.append(mvstr[a])
        a = a + 1
    return clq

def howmanyhouses(c,mstr):
    return len(getuniq(c,mstr))

print(howmanyhouses([0,0], "^^^v"))

#print(isitinlist([1,2,3], 2))