import cv2
import numpy

print()
print("-------- Reading an image file using numpy (Greyscale) --------------------")
print()

# Read the Image in Greyscale             V
im_g = cv2.imread("Images/smallgray.png", 0)
print(im_g)
print()
print("-------- Reading an image file using numpy (Colour) ---------------------")
print()
# Read the Image in Colourr               V
im_c = cv2.imread("Images/smallgray.png", 1)
print(im_c)


# Creating an image ...
cv2.imwrite("Images/newsmallgrey.png", im_g)

print()
print("--------- Slicing numpy arrays --------------------")
print()

# Slicing numpy arrays
# Select the first 2 rows and then columns 3 and 4
sliceone = im_g[0:2, 2:4]
print(sliceone)

print()
print("-------- Iterating through numpy arrays (Rows) ---------------------")
print()

# Iterating through numpy arrays (this goes through the rows)
for i in im_g:
    print(i)
print()
print("-------- Iterating through numpy arrays (Columns) ---------------------")
print()

# Iterating through numpy arrays (this goes through the columns via 'transpose')
for i in im_g.T:
    print(i)
print()
print("-------- Iterating through numpy arrays (each value) ---------------------")
print()

# Iterating through numpy arrays (this goes through each value via 'flat')
for i in im_g.flat:
    print(i)

print()
print("-------- Stacking numpy arrays (horizontally) ---------------------")
print()
# Staking numpy arrays
imstackedone = numpy.hstack((im_g, im_g))
print(imstackedone)

print()
print("-------- Stacking numpy arrays (vertically) ---------------------")
print()
# Staking numpy arrays
imstackedtwo = numpy.vstack((im_g, im_g))
print(imstackedtwo)

print()
print("-------- Splitting numpy arrays (horizontally) ---------------------")
print()
# Staking numpy arrays
imsplitone = numpy.hsplit(imstackedtwo, 5)
print(imsplitone)

print()
print("-------- Splitting numpy arrays (vertically) ---------------------")
print()
# Staking numpy arrays
imsplittwo = numpy.vsplit(imstackedtwo, 3)
print(imsplittwo)
