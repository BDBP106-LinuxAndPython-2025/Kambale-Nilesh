#!/usr/bin/python3
from setuptools.dist import sequence


# (7) Write a function analyse_dna(sequence) that defines an inner function gc_content()
# to calculate GC% . The outer function should print whether the given DNA is AT rich
# or GC rich sequence.


def analyse_dna(sequence):
    def gc_content(seq):
        gc = seq.count('G') + seq.count('C')
        return (gc / len(seq)) * 100

    gc_percent = gc_content(sequence.upper())
    if gc_percent > 50:
        print("GC-rich sequence")
    else:
        print("AT-rich sequence")

sequence=input("Enter sequence to analyse: ")
analyse_dna(sequence)

