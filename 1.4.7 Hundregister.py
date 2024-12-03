

hundregister = []

while True:
    print("1. Mata in hundar")
    print("2. Avsluta")
    menyval=input(":")

    if menyval=="1":
        Namn=input ("Vad heter din hund ? \n")
        Ras=input ("Vad är din hund för ras ? \n")
        Vikt=input ("Vad väger din hund ? \n")
        hundregister.append({"Namn":Namn, "Ras":Ras, "Vikt":Vikt})
    else:
        break

print (hundregister)