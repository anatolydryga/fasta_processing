#!/usr/bin/python

import argparse
from Bio import SeqIO

def average_read_length(fasta_fh):
    read_length = get_sequence_length(fasta_fh)
    return sum(read_length)/float(len(read_length))

def get_sequence_length(fasta_fh):
    seq_length = []
    for record in SeqIO.parse(fasta_fh, "fasta"):
        seq_length.append(len(record))
    return seq_length

if __name__=="__main__":
    parser = argparse.ArgumentParser("Average read length for fasta files")
    parser.add_argument('fasta_files', nargs='+', type=argparse.FileType('r'))
    args = parser.parse_args()

    for fasta in args.fasta_files:
        average = average_read_length(fasta)
        print fasta.name + "\t" + str(average)
