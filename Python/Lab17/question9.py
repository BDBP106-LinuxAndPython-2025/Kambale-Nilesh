#(9) A DNA sequence encodes each amino acid making up a protein as a three-nucleotide
#sequence called a codon. For example, the sequence fragment AGTCTTATATCT contains the codons AGT,
# CTT, ATA, TCT if read from the first position. If read from
#the second position, it yields the codons GTC, TTA, TAT and if read from the third
#position we get TCT, TAT, ATC. Write a function to extract the codons into a list of
#3-letter strings given a sequence and from what position (input as an integer) the
# sequence should be read. As an example, output the 3-letter strings from the sequence
#GTTTCGATTATAACG read from the (i) 1st position and (ii) 3rd position.
def codon(seq, pos):
    cod=[]
    for i in range(pos-1,len(seq),3):
        c=seq[i:i+3]
        if len(c)==3:
            cod.append(c)
    return cod
seq=input("Enter the sequence: ")
print(codon(seq,1))
print(codon(seq,3))



