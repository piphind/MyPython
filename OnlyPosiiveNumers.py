def extractpositive(inlist):
    outlist = [element for element in inlist if element > 0]
    return(outlist)

outlist = extractpositive([-1,0,-3,2,-7,4, -5, 5, 6, -1, 0])
print(outlist)
