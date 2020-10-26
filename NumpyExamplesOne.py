import numpy

# 1 Dimensional Array
n0 = numpy.arange(27)
print(type(n0))
print(n0)

# 2 Dimensional Array by reshaping
n1 = n0.reshape(3, 9)
print(n1)

# 3 Dimensional Array by reshaping
n2 = n0.reshape(3, 3, 3)
print(n2)

m0 = numpy.asarray([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(type(m0))
print(m0)
