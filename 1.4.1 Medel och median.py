print ("Skriv gärna 5 tal")
talList = [0,0,0,0,0]
for i in range(5):
    talList[i]=int (input("Ange ett tal: "))


talList.sort()

print ("Dina tall är" ,(talList))

meat = sum(talList) / len(talList)
ribs = talList [2]

print("Medelvärdet är:", meat)
print("Medianen är:", ribs)
