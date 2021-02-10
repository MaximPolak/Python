def vraceni_prvku(*args):
    def nekonecno():
        i = 0
        while True:
            yield i
            i += 1
    for j in nekonecno():
        for objekt in args:
            try:
                yield objekt[j]
            except IndexError:
                return None