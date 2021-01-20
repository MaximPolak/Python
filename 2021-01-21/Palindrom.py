def palindrom_smyckou(slovo):
    delka = len(slovo) - 1
    i = 0
    while i < delka:
        if slovo[i] == slovo[delka]:
            i= i + 1
            delka = delka - 1
            if i == delka or i + 1 == delka:
                return True
        else:
            return False

def palindrom_rekurzivne(slovo):
    print(slovo)
    if len(slovo) == 1 or 0:
        return True
    elif slovo[0] != slovo[-1]:
        return False
    else:
        return palindrom_rekurzivne(slovo[1:-1])