#!/usr/bin/python

import argparse

from Bio import SeqIO

def number_of_reads(filename):
    number_of_reads = 0
    for record in SeqIO.parse(filename, "fasta"):
        number_of_reads += 1
    return number_of_reads

if __name__=="__main__":
    parser = argparse.ArgumentParser("Number of reads for fasta files")
    parser.add_argument('fasta_files', nargs='+', type=argparse.FileType('r'))
    args = parser.parse_args()

    for fasta in args.fasta_files:
        print fasta.name + "\t" + str(number_of_reads(fasta))
