myTup=(3,6,8,2,4,6,1,6,7,8,4,5,2,6,9)
Biggie=0
Smalls=0
for tal in myTup:
    if tal > Biggie:
        Biggie=tal

Smalls=Biggie
for tal in myTup:
    if tal < Smalls:
        Smalls=tal
print ("Det största talet är" ,Biggie)
print ("Det minsta talet är" ,Smalls)