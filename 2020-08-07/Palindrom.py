slovo = input("Zadejte slovo: ")

def je_palindrom(slovo):
    if slovo == slovo[::-1]: 
        return True
    else:
        return False