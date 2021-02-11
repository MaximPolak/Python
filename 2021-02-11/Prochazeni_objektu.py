def vraceni_prvku(*args):
    seznam = list(iter(i) for i in args)

    while True:
        try:
            for objekt in seznam:
                yield next(objekt)
        except StopIteration:
            break