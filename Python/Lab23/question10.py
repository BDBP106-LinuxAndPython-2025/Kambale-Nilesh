# (10) Take a DNA sequence and determine whether or not it contains any ambiguous bases –
# i.e. any bases that are not A, T, G or C. If there is a non ambiguous base, print the non
# ambiguous bases. dna = ”ATCGCGYAATTCAC”
import re

dna = "ATCGCGYAATTCAC"
pattern = r"[YU]"

matches = list(re.finditer(pattern, dna))
if matches:
    for match in matches:
        print(f'{match.group()} | Non-ambiguous base at position : {match.start()} | ')
else:
    print("No such base found!.")