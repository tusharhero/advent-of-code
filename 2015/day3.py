#https://adventofcode.com/2015/day/3
#TUSHAR MAHARANA
#tusharhero.mit-license.org

#lets a cartesian system to do this.

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
