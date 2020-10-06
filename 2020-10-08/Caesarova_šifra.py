import sys
def caesarova_sifra(slovo, posun): 
    sifra = "" 
    if posun < -25 or posun > 25:
        sys.stderr.write(sys.stdout)
        return None
    if posun == 0:
        print("Pozor, slovo zůstane stejné")
    else:
        for pismeno in slovo: 
            if ord(pismeno) > 64 and ord(pismeno) < 91:
                sifra += chr((ord(pismeno) + posun - 65) % 26 + 65)  
            elif ord(pismeno) > 96 and ord(pismeno) < 123:
                sifra += chr((ord(pismeno) + posun - 97) % 26 + 97)
            else:
                sifra += pismeno
  
    return sifra 