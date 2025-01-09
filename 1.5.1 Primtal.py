import math
while True:
    # Läs in ett tal och avbryt om användaren vill sluta
    s = input ("Talet? ")
    if s == '':
        break
    else:
        talet = int(s)
    # Undersök om talet är ett primtal
    # Skriv ut resultatet

    for i in range(2, talet):
        if (talet%i == 0):
            quit (str(talet) + " is not a prime number")
    print (talet, "is a prime number") 


