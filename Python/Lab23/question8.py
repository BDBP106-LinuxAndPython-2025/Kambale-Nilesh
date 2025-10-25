# (8) Check for the presence of an AvaII recognition site, which can have two different se-
# quences: GGACC and GGTCC. Use regular expressions. dna = ”ATCGCGAATTCAC”
# pattern = GGACC and GGTCC
import re

dna = "ATCGCGAATTCACGGTCC"
pattern = r"GGACC|GGTCC"

matches = list(re.finditer(pattern, dna))

if matches:
    print("Given DNA sequence contains the AvaII Restriction site:")
    for match in matches:
        print(f'{match.group()} | start: {match.start()} | end: {match.end()}')
else:
    print("Given DNA sequence does not contain the AvaII Restriction site.")
