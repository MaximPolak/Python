def je_palindrom(slovo):
    if slovo == slovo[::-1]: 
        return True
    else:
        return False

assert je_palindrom("radar")
assert je_palindrom("míč") == False

slovo = input("Zadejte slovo: ")

if je_palindrom(slovo): 
    print("JE to palindrom")
else:
    print("NENÍ to palindrom")