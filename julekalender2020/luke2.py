import numpy, julekalender2020

#10 => 7
#20 => 9
#10000 => 32
#5433000 =>

allepakker = list(range(0,5433000,1))
kastedepakker = []

for pakke in allepakker:
    
    if julekalender2020.isPrime(pakke):
            lastprime = pakke

    if (pakke in kastedepakker):
        continue
    
    if (str('7') in str(pakke)):
        kastedepakker.extend(allepakker[pakke:pakke+lastprime+1])
      
levertepakker = numpy.setdiff1d(allepakker, kastedepakker)

print("Antall leverte pakker: ", len(levertepakker))
print(levertepakker)

