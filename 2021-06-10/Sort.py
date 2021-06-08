import argparse, sys
ctecka = argparse.ArgumentParser(description="sort lines of text files")

ctecka.add_argument("files", default="sys.stdin", help="sort FILE(s) (with no FILE, sort standard input)")
ctecka.add_argument("--reverse", "-r", action="store_true", help="reverse the result of comparisons")
ctecka.add_argument("--start", "-s", type=int, default=1, help="start comparisons from the character position START (counting from 1)")
ctecka.add_argument("--output", "-o", default=sys.stdout, help="write to OUTPUT instead of standard output")

args = ctecka.parse_args()

def sort(co, reverse, start):
    if co != "sys.stdin":
        radky = []
        with open(co, 'r') as soubor:
            for radek in soubor:
                radky.append(radek)
    else:
        radky = sys.stdin.read().split()

    if start != 1:
        radky = radky[0:start - 1] + sorted(radky[start - 1:])
    else:
        radky = sorted(radky)
    
    if reverse:
        radky = reversed(radky)
    
    for radek in radky:
        yield radek

for i in sort(args.files, args.reverse, args.start):
    args.output.write(i + "\n")