import numpy

hiddenwords_orig = numpy.genfromtxt('julekalender2020/luke3/matrix.txt',dtype=str)

hiddenwords_transposed = []
for i in range(len(hiddenwords_orig[0])):
    new_string = ''.join([line[i] for line in hiddenwords_orig])
    hiddenwords_transposed.append(new_string)

hiddenwords_chararray = numpy.chararray((1000,1000), unicode=True) 
for i in range(len(hiddenwords_orig[0])):
    hiddenwords_chararray[i] = numpy.char.array(hiddenwords_orig[i], itemsize=1)




wordlist = numpy.genfromtxt('julekalender2020/luke3/wordlist.txt', dtype=str)
wordsfound = []

for word in wordlist:

    for row in hiddenwords_orig:
        if word in row:
            wordsfound.append(word)
            print("Found word, correct way: ", word)

        if str(word)[::-1] in row:
            wordsfound.append(word)
            print("Found word, reversed: ", word)

    for row in hiddenwords_transposed:
        if word in row:
            wordsfound.append(word)
            print("Found word, transposed, correct way: ", word)

        if str(word)[::-1] in row:
            wordsfound.append(word)
            print("Found word, transposed, reversed: ", word)

        
print("Size hiddenwords: ", len(hiddenwords_orig))
print("Size wordlist: ", len(wordlist))
print("Size wordsfound: ", len(wordsfound))
print(wordsfound)

print("Shape of orig", numpy.shape(hiddenwords_orig))
print("Shape of transposed: ", numpy.shape(hiddenwords_transposed))
print("Shape of chararray: ", numpy.shape(hiddenwords_chararray))
print(hiddenwords_chararray[0,1000])
