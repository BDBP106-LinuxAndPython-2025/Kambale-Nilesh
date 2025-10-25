# 9) Check for the presence of a BisI restriction site using regular expression character groups:
# A character group is a pair of square brackets with a list of characters inside them. dna
# = ”ATCGCGAATTCAC” pattern = GCNGC, where N represents any base, i.e. A, T,
# G, C
import re

dna = "ATCGCGAATTCAC"
pattern = r"GC[ATGC]GC"
matches = list(re.finditer(pattern, dna))
if matches:
    print("Given DNA sequence contains the BisI Restriction site:")
    for match in matches:
        print(f'{match.group()} | start: {match.start()} | end: {match.end()}')
else:
    print("Given DNA sequence does not contain the BisI Restriction site.")