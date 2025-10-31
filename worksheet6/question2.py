# (2) Here’s a DNA sequence with the bits that we want to extract in bold: ACTGCAT-
# TATATCGTACGAAATTATACGCGCG Extract the bits of the string that match the
# pattern (highlighted in bold) using findall():
import re

seq = "ACTGCATTATATCGTACGAAATTATACGCGCG"

pat = r'(?:TATA|CGCG)'
matches = re.findall(pat, seq)

print("DNA sequence:", seq)
print("Extracted pattern/motif:", matches)
