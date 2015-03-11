from Bio import SeqIO

def filter_short_reads(filename, min_length, filtered_fasta):
    handle = open(filename)
    output = open(filtered_fasta, 'w')
    surviving_reads = 0
    for record in SeqIO.parse(handle, "fasta"):
        if len(record) > min_length:
            SeqIO.write(output, record, "fasta")
            surviving_reads += 1
    handle.close()
    return surviving_reads

if __name__=="__main__":
    parser = argparse.parser("Filtering reads for fasta files")
    parser.add_argument()
    parser.add_argument()

    args = parser.parse()

    for fasta in args.fasta_files:
        surviving_reads = filter_short_reads(fasta, min_length, output_fasta)
        print fasta + "\t" + str(surviving_reads)
