def bubble_sort(seznam):
    """
    [6, 5, 8, 1]
    5, 6, 8, 1
    5681
    5618
    2.kolo
    5618
    5168
    5168
    3.kolo
    1568
    """

    for i in range(len(seznam)):
        for aktualni_cislo in range(len(seznam) - 1):

            if seznam[aktualni_cislo] > seznam[aktualni_cislo + 1]:
                seznam[aktualni_cislo], seznam[aktualni_cislo + 1] = seznam[aktualni_cislo + 1], seznam[aktualni_cislo]

    return(seznam)

seznam = [6, 5, 8, 1]
print(bubble_sort(seznam))

