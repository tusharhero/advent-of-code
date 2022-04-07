#https://adventofcode.com/2015/day/1
#TUSHAR MAHARANA
#tusharhero.mit-license.org
def getfloor(l,B):#decides which floor to go now
    if B == "(":
        l = l + 1
    if B == ")":
        l = l - 1
    return l

def getlastfloor(st):
    L = len(st)
    a = 0
    f = 0
    while a < L:
        f = getfloor(f,st[a])
        a = a + 1
    return f


#test = ""

print(getlastfloor(test))