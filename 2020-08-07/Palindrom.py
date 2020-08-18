slovo = input("Zadejte slovo: ")

if slovo == slovo[::-1]: 
    print("JE to palindrom")
else:
    print("NENÍ to palindrom")