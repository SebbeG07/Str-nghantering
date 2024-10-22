TempList = []


while True:
    
    Temp = input ("Mata in en temperatur: ")
    
    
    if Temp.lower() == '':
        break
    else:
        TempList.append(float(Temp))

print (len(TempList), "Antal värden")
sum=0
for temp in TempList:
    sum+=temp
celsius2= (sum / len(TempList))
print("MedelTemperaturen är", sum / len(TempList),"°C")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = celsius2
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C är lika med {fahrenheit}°F")