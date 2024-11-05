TalList = []


while True:
    
    Tal = input ("Mata in heltal: ")
    
    
    if Tal.lower() == '':
        break
    else:
        TalList.append(int(Tal))
print (len(TalList), "Antal värden")
TalList.sort()
print(TalList)
isSame=False
for i in range (len(TalList)-1):
    if TalList[i]==TalList[i+1]:
        isSame=True
        break
    else:
        isSame=False
if isSame:
    print ("Det finns dubbletter!!")
else:
    print ("Det finns inte dubbleter")