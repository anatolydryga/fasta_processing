from Bio import SeqIO

def number_of_reads(filename):
    handle = open(filename)
    number_of_reads = 0
    for record in SeqIO.parse(handle, "fasta"):
        number_of_reads += 1
    handle.close()
    return number_of_reads

if __name__=="__main__":
    parser = argparse.parser("Number of reads for fasta files")
    parser.add_argument()

    args = parser.parse()

    for fasta in args.fasta_files:
        number_of_reads = number_of_reads(fasta)
        print fasta + "\t" + str(number_of_reads)
