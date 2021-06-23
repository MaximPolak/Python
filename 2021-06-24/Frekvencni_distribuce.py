import argparse, sys
ctecka = argparse.ArgumentParser()

ctecka.add_argument("files", default=(sys.stdin,), nargs="*", type=argparse.FileType())
ctecka.add_argument("--min", "-m", default=-1, type=int)
ctecka.add_argument("--ignore-case", "-i", action="store_true")
ctecka.add_argument("--alphabetical", "-a", action="store_true")
ctecka.add_argument("--output", "-o", default=sys.stdout, type=argparse.FileType("w"))

args = ctecka.parse_args()

def spocti_slova(soubory, ignore_case):
    frekvence = {}
    for soubor in soubory:
        with soubor:
            obsah_souboru = "".join(soubor.readlines()).split()
        for slovo in obsah_souboru:
            if ignore_case:
                slovo = slovo.lower()
            if slovo not in  frekvence:
                frekvence[slovo] = 1
            else:
                frekvence[slovo] += 1
    return frekvence

frekvence_slov = spocti_slova(args.files, args.ignore_case)
maximalni_frekvence = len(str(max(frekvence_slov.values())))

if not args.alphabetical:
    poradi_slov = sorted(frekvence_slov.items(), key=lambda x: (-x[1], x[0]))
else:
    poradi_slov = sorted(frekvence_slov.items())

with args.output as soubor:
    for slovo, pocet in poradi_slov:
        if pocet != -1 and pocet >= args.min:
            soubor.writelines(f"{str(pocet).rjust(maximalni_frekvence)} {slovo}\n")
