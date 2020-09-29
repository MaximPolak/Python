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
    puvodni_seznam = seznam

    for i in range(len(seznam)):
        for j in range(len(seznam) - 1):

            if sorted(seznam) == seznam:
                break

            if seznam[j] > seznam[j + 1]:
                # seznam[j], seznam[j + 1] = seznam[j + 1], seznam[j]
                j_vetsi_kopie = seznam[j + 1]
                j_kopie = seznam[j]
                seznam[j] = j_vetsi_kopie
                seznam[j + 1] = j_kopie           

    return seznam

seznam = [6, 5, 8, 1]
print(bubble_sort(seznam))

