


#lektion 2
def uppgift8(time_in_mins, speed_in_KMperH):
    time = time_in_mins
    speed = speed_in_KMperH
    length = speed*(time/60)
    print(length, "km") 
    return length




def uppgift9(sträcka):
    sträckaiM = sträcka/100
    print(sträckaiM, "m")
    return sträckaiM





def uppgift10(SEK):
    USD = (SEK/10.17)
    print(USD, "USD")
    return USD






def uppgift11(Temp, FToC: bool):
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
#vilken uppgift som ska köras / kalla funktion
uppgift11(20, False)
