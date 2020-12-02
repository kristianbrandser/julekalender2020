import numpy, julekalender2020

#allepakker = numpy.arange(0,20,1,dtype=int)
# 5433000
# mask med alle pakker som skal kastes, 
# dvs. iterere gjennom array og ved siffer 7 så 
# skal pakken kastes + antall nærmeste primtall, 
# som er mindre eller lik pakkenummeret
allepakker = list(range(0,10000,1))
kastedepakker = []
lastPrime = 0

for pakke in allepakker:
    
    if (pakke not in kastedepakker):
        if (julekalender2020.isPrime(pakke)):
            lastPrime = pakke

    if (str('7') in str(pakke)):
        # Santa sad
        kastedepakker.extend(allepakker[pakke:pakke+lastPrime+1])
      
levertepakker = numpy.setdiff1d(allepakker, kastedepakker)

print("Antall leverte pakker: ", len(levertepakker))
print(levertepakker)
print("Totalt antall pakker: ", len(allepakker))
print("Antall kastede pakker: ", len(kastedepakker))
#print(kastedepakker)

