# (7) Test if a DNA sequence contains an EcoRI restriction site using regular expressions. dna
# = ”ATCGCGAATTCAC” pattern = GAATTC
import re

seq="ATCGCGAATTCAC"
pattern= r"GAATTC"
reseq=re.finditer(pattern,seq)
for match in re.finditer(pattern,seq):
    if match.group() in seq:
        print(f'Given DNA sequence contain the EcoRI Restriction site ')
        print(f'{match.group()} | start: {match.start()} | end: {match.end()}')
