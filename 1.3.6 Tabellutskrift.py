print ("Tal".rjust(15), "Kvadrat".rjust(15), "Kubik".rjust(15))
for tal in range(1, 11):
    kvadrat = tal ** 2  
    kubik = tal ** 3    
    
   
    print(str(tal).rjust(14), str(kvadrat).rjust(13), str(kubik).rjust(16))
    

# Om man vill ha en egen range :)
test=int (input ("Skriv en range: "))
print ("Tal".rjust(15), "Kvadrat".rjust(15), "Kubik".rjust(15))
for tal in range(1, test+1 ):
    kvadrat = tal ** 2  
    kubik = tal ** 3    
    
   
    print(str(tal).rjust(14), str(kvadrat).rjust(13), str(kubik).rjust(16))