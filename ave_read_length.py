from Bio import SeqIO

def average_read_length(filename):
    handle = open(filename)
    read_length = []
    for record in SeqIO.parse(handle, "fasta"):
        read_length.append(len(record))
    return read_length

if __name__=="__main__":
    parser = argparse.parser("Average read length for fasta files")
    parser.add_argument()

    args = parser.parse()

    for fasta in args.fasta_files:
        average_read_length = average_read_length(fasta)
        print fasta + "\t" + str(average_read_length)
