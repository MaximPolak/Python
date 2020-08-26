def linearne_vyhledej(hodnota, seznam):
    for i, h in enumerate(seznam):
        if h == hodnota:
            return i
    return -1

def test_linearne_vyhledej():
    seznam = [0,1,1,1,5]
    assert linearne_vyhledej(0, seznam) == 0
    assert linearne_vyhledej(2, seznam) == -1