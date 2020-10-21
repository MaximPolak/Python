def bubble_sort(seznam):
    serazena_cast = []

    for i in range(len(seznam) - 1):
        zmeny = False

        for j in range(len(seznam) - 1):
            if seznam[j] > seznam[j + 1]:
                seznam[j], seznam[j + 1] = seznam[j + 1], seznam[j]
                zmeny = True
        if zmeny == False:
            break
        serazena_cast.insert(0, seznam[-1])
        seznam.pop(-1)
    return seznam + serazena_cast
