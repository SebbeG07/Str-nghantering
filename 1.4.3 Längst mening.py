mean = []
for i in range(5):
    mening = input("Skriv in mening: ")
    i + 1
    mean.append(mening)

meanlength = [len(mening) for mening in mean]

yesmean = sum(meanlength) / len(mean)

maxmean = max(meanlength)
print ("Medellängden på alla meningar är" ,yesmean )
print ("Den längsta meningen är" ,maxmean , "tecken lång")