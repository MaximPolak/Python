def prevrat(slovnik):
    """Funkce pro daný slovník vrací slovník, kde jsou klíči původní hodnoty a hodnotami seznam původních klíčů. """
    slovnik = slovnik.copy()
    prevraceny_slovnik = {}

    for klic in slovnik:
        seznam = []
        seznam.append(slovnik[klic])

        for hodnota in seznam:
            if hodnota not in prevraceny_slovnik:
                prevraceny_slovnik[hodnota] = []
            prevraceny_slovnik[hodnota].append(klic)

    return prevraceny_slovnik
