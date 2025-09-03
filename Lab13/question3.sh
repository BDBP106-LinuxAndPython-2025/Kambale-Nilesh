#!/bin/bash
#(i) Using gawk remove the lines containing >. These are called header lines.
echo "Answer of (i)"
gawk '$0 !~/^>/' fasta.txt
echo""

#(ii) Using sed convert the DNA sequence to RNA sequence.
echo "Answer of (ii)"
sed 's/T/U/g' fasta.txt
echo""

#(iii) Using sed replace seq1 (called the sequence ID) by human_gene.
echo "Answer of (iii)"
sed 's/^>seq1/human_gene/' fasta.txt
