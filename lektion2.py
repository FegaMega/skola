import math


#lektion 2
def uppgiftLEK2UPP8(time_in_mins, speed_in_KMperH):
    time = time_in_mins
    speed = speed_in_KMperH
    length = speed*(time/60)
    print(length, "km") 
    return length




def uppgiftLEK2UPP9(sträcka):
    sträckaiM = sträcka/100
    print(sträckaiM, "m")
    return sträckaiM





def uppgiftLEK2UPP10(SEK):
    USD = (SEK/10.17)
    print(USD, "USD")
    return USD






def uppgiftLEK2UPP11(Temp, FToC: bool):
    if FToC == False: 
        F = (Temp*1.8)+32
        print(F, "Fahrenheit")
        return F
    elif FToC == True:
        C = (Temp-32)/1.8
        print(C, "Celcius")
        return C
    elif FToC != None:
        print("FToC är en", type(FToC), "och ska vara en bool")
        return 1
    else:
        print("FToC är inte ifylld")
        return 2
def uppgiftLEK3UPP1():
    text = input("ålder: ")
    längd = input("längd: ")
    print(3* text, 3*längd)

def uppgiftLEK3UPP2():
    print(round(46.987123, 1))

def uppgiftLEK3UPP3():
    text = int(input("Ålder: "))
    print(220 - text)
    return 
    
#uppgiftLEK3UPP4
#A)Kvadratens area är 6.25 kvadratcentimeter.
#B)

#uppgiftLEK3UPP9
#Hon multiplicerar en str med 0.8 vilket inte går
#hon måste göre det till en float eller int

def uppgiftLEK3UPP10A():
    diameter = float(input("diameter: "))
    print(diameter * math.pi)

def uppgiftLEK3UPP10B():
    radien = float(input("radien: "))
    print(radien**2 * math.pi)

def uppgiftLEK3UPP15():
    chokladbitar = int(input("Hur många choklad bitar vill du köpa? "))
    chokladKostnad = 12
    askKostnad = 20
    if chokladbitar != None:
        print("Det skulle kosta ", chokladKostnad*chokladbitar + askKostnad, "kr")

def uppgiftLEK9UPP14():
    output = [0, 1]
    for i in range(0, 100):
        output.append(int(output[i] + output[i+1]))
    print(output)
    return output

#vilken uppgift som ska köras / kalla funktion

uppgiftLEK3UPP10B()
