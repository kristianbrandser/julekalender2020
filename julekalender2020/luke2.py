import numpy
from julekalender2020 import isPrime

#10 => 7
#20 => 9
#10000 => 32
#5433000 =>

allepakker = list(range(0,5433000,1))
kastedepakker = []
lastprime = 0

for pakke in allepakker:
    
   # if julekalender2020.isPrime(pakke):
   #         lastprime = pakke

    if (pakke in kastedepakker):
        continue
    
    if (str('7') in str(pakke)):

        #for i in range(lastprime, pakke+1):
        #    if isPrime(i):
        #        lastprime = i
        
        fantprime = False
        i = pakke

        while not fantprime:
                if isPrime(i):
                    lastprime = i
                    fantprime = True
                else:
                    i -= 1

        kastedepakker.extend(allepakker[pakke:pakke+lastprime+1])
      
levertepakker = numpy.setdiff1d(allepakker, kastedepakker)

print("Antall leverte pakker: ", len(levertepakker))
print(levertepakker)

