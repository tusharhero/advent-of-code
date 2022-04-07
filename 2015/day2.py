#https://adventofcode.com/2015/day/2
#TUSHAR MAHARANA
#tusharhero.mit-license.org
def surfacearea(l,w,h):#simple function for surface area
    sa = l*w+l*h+w*h
    sa = 2*sa
    return sa

def findsmallest(l,w,h):#finds the smallest side
    a = l*w #getting the areas (all this could be done in a single function thoo)
    b = l*h 
    c = w*h
    if a <= b:# if a is smaller than b then
        if a <= c: # check if a is also smaller than c
            return a # if yes a is the side we need :)
        else:# if no :(, then 
            if b <= c: #check if b is smaller than c, we already know that a is bigger then both of them so let us not worry about it.
                return b #if it smaller then return
            else:# if no, it just means that c is the smallest, as it is the only one left
                return c

def wrappingarea(l,w,h):
    sa = surfacearea(l,w,h) + findsmallest(l,w,h)#add'em as per the rule
    return sa

#driver
l = 1
w = 3
h = 5
print(wrappingarea(l,w,h))