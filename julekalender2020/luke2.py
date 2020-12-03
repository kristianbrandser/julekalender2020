import numpy, sympy
#from julekalender2020 import isPrime

#10 => 7
#20 => 9
#10000 => 32
#100000 => 51?
#5433000 => 

allepakker = list(range(0,5433000,1))
kastedepakker = []
lastprime = 0
nLevertepakker = 0

for pakke in allepakker:
    
   # if julekalender2020.isPrime(pakke):
   #         lastprime = pakke

    if (pakke in kastedepakker):
        continue
    
    if (str('7') in str(pakke)):

        #for i in range(lastprime, pakke+1):
        #    if isPrime(i):
        #        lastprime = i
        
        ##fantprime = False
        ##i = pakke

        ##while not fantprime:
        ##        if isPrime(i):
        ##            lastprime = i
        ##            fantprime = True
        ##        else:
        ##            i -= 1
        lastprime = sympy.prevprime(pakke+1)
        nLevertepakker = pakke - len(kastedepakker) 
        kastedepakker.extend(allepakker[pakke:pakke+lastprime+1])
        

#Slow?   
#levertepakker = numpy.setdiff1d(allepakker, kastedepakker)

#print("Antall leverte pakker: ", len(levertepakker))
print("Antall leverte pakker: ", nLevertepakker)
#print(levertepakker)

