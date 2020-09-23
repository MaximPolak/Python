with open("babicka.txt", encoding = "utf-8") as soubor:
    cely_text = soubor.read()
    slova = set(cely_text.split())

def najdi_minimalni_pary(slova):
    slovnik = {}

    for slovo1 in slova:
        for slovo2 in slova:
            if len(slovo1) == len(slovo2):
                rozdily = 0
                for (znak1, znak2) in zip(slovo1, slovo2):
                    if znak1 != znak2:
                        rozdily += 1
                        if znak1 < znak2:
                            lisici_se_znaky = (znak1, znak2)
                        else:
                            lisici_se_znaky = (znak2, znak1)
                if rozdily == 1:
                    if lisici_se_znaky not in slovnik:
                        slovnik[lisici_se_znaky] = []

                    slovnik[lisici_se_znaky].append((slovo1, slovo2))
    
    return slovnik           
            
print(najdi_minimalni_pary(slova))