import numpy

numbersfromfile = numpy.genfromtxt("julekalender2020/luke1/numbers.txt", dtype=int, delimiter=',')
allnumbers = numpy.arange(1,100000,1,dtype=int)
mask = numpy.isin(allnumbers, numbersfromfile, assume_unique=True, invert=True)
print(allnumbers[mask])

# 81273