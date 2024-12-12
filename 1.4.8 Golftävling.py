
golfregister = []

while True:
    print("1. Mata in deltagare")
    print("2. Vissa alla deltagare")
    print("3. Avsluta")

    menyval=input(":")

    if menyval=="1":
        Namn=input ("Vad heter deltageren ? \n")
        Slag=input ("Hur många slag ? \n")
        Handikapp=input ("Hur många slag var handikapp ? \n")
        golfregister.append({"Namn":Namn, "Slag":Slag, "Handikapp":Handikapp})
    elif menyval=="2":
        print (golfregister)
    elif menyval=="3":
        break

print (golfregister)