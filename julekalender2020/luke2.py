import numpy, julekalender2020

allepakker = numpy.arange(0,10,1,dtype=int)
# 5433000
# mask med alle pakker som skal kastes, 
# dvs. iterere gjennom array og ved siffer 7 så 
# skal pakken kastes + antall nærmeste primtall, 
# som er mindre eller lik pakkenummeret
kastedepakker = []
for pakke in allepakker:

    if (julekalender2020.isPrime(pakke)):
        lastPrime = pakke

    if (str('7') in str(pakke)):
        # Santa sad
        kastedepakker.extend(range(pakke, pakke+lastPrime+1))
      
levertepakker = numpy.setdiff1d(allepakker, kastedepakker)
print("Antall leverte pakker: ", numpy.size(levertepakker))

print("Kastede pakker")
print(kastedepakker)