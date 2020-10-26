def createintlist(inlist):
    outlist = [element if not isinstance(element, str) else 0 for element in inlist]
    return(outlist)

print(createintlist([99,'no data', 95, 94, 'no data']))

