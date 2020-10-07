def bubble_sort(seznam):

    for i in range(len(seznam) - 1):
        zmeny = False

        for j in range(len(seznam) - 1):
            if seznam[j] > seznam[j + 1]:
                seznam[j], seznam[j + 1] = seznam[j + 1], seznam[j]
                zmeny = True
        if zmeny == False:
            break
    return seznam

