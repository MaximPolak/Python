def linearne_vyhledej(hodnota, seznam):
    for i in range(len(seznam)):
        if seznam[i] == hodnota:
            return i
    return -1 
        

