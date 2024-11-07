Test= input ("Skriv gärna en mening: ")
lista = Test.split(' ')
print (f"Orden i din mening är\n",lista)
print ("Din mening består av",len(lista),"ord")
numWords=0
for i in lista:
    if len(i)>=5:
       numWords +=1
print ("Antal ord över fem tecken:", numWords)