import sys, argparse

ctecka = argparse.ArgumentParser(description="print lines of standard input that match a pattern")

ctecka.add_argument("pattern", help="matched string")
ctecka.add_argument("--invert-match", "-v", action="store_true", help="print non-matching lines instead")
ctecka.add_argument("--ignore-case", "-i", action="store_true", help="ignore case distinctions in a pattern")
ctecka.add_argument("--max", "-m", type=int, default=0, help="print at most MAX matching lines")

args = ctecka.parse_args()

def find(retezec, kde, invert, ignore, pocet_vyskytu=0):
    if pocet_vyskytu == 0:
        return
    
    if ignore:
        retezec = retezec.upper()
    
    for radek in kde:
        if (retezec in (radek if not ignore else radek.upper())) ^ invert:
            yield radek
            pocet_vyskytu -= 1
            if pocet_vyskytu == 0:
                return    

for i in find(args.pattern, sys.stdin, args.invert_match, args.ignore_case, args.max):
    print(i, end="")
    