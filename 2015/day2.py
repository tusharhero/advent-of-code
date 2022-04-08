#https://adventofcode.com/2015/day/2
#TUSHAR MAHARANA
#tusharhero.mit-license.org

def findareaind(l,w,h):#this function gets the area of individual faces
    a = l*w
    b = l*h 
    c = w*h
    return [a,b,c]


def surfacearea(l,w,h):#simple function for surface area
    sal = findareaind(l, w, h)
    sa = 2*(sal[0]+sal[1]+sal[2])
    return sa

def findsmallest(l,w,h):#finds the smallest side
    sal = findareaind(l, w, h)
    a = sal[0] #getting the areas using the function we made
    b = sal[1]
    c = sal[2]
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
w = 1
h = 10
print(wrappingarea(l,w,h))