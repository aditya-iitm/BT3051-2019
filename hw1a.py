# BT3051 Assignment 1a
# Roll number: BS16B001
# Collaborators: Nil
# Time: 2 hours

import sys

def read_fasta(fname):
    # (str) -> (list of tuples)
    # This function reads the given fasta file and returns a list of tuples 
    # of the form (sequence_name , sequence)
    sequences = []
    name = ''
    sequence = ''
    with open(fname) as f:
        for line in f.readlines():
            if line[0] == '>':
                sequences.append((name,sequence))
                name = line[1:].strip()
                sequence = ''
            else:
                sequence += line.strip()
        sequences.append((name,sequence))

    return sequences[1:]

def ret_ORF(dna_sequence):
    """
    # (str) -> (str)
    # This function takes an individual DNA strand and returns a string containing
    # all the open reading frames in the given strand, separated by spaces, i.e., it
    # identifies all the pairs of start and stop codons in the frame and prints 
    # the appropriate strand.

    >>> ret_ORF('GTCATGGAAGCCTAAGCTATGCCATAG')
    'ATGGAAGCCTAA ATGCCATAG'
    >>> ret_ORF('TGGCCT')
    'None'
    """
    sequences = []
    flag = 0
    stop = ['TAA','TAG','TGA']
    for i in range(len(dna_sequence)//3):
        if dna_sequence[3*i:3*i+3] == 'ATG' and flag == 0:
            flag = 1
            start = i
        if flag == 1 and dna_sequence[3*i:3*i+3] in stop:
            sequences.append(dna_sequence[3*start:3*i+3])
            flag = 0
    if len(sequences) == 0:
        return 'None'
    else:
        return ' '.join(sequences)



def revc(string):
    # This function returns the reverse complement of the given dna sequence as a string
    comp = {'A':'T','T':'A','G':'C','C':'G'}
    new = ''
    for i in range(len(string)):
        new += comp[string[i]]
    return new[::-1]

def get_orientations(dna_sequence):
    """
    # (str) -> (list of strings)
    # This function takes a DNA sequence and returns the six possible reading
    # frames for the sequence, 3 on the strand and 3 on the reverse complement.
    # It has also been ensured that the strands have a length, multiple of three.
    >>> get_orientations('AATGGCCTAA')
    ['AATGGCCTA', 'ATGGCCTAA', 'TGGCCT', 'TTAGGCCAT', 'TAGGCCATT', 'AGGCCA']
    """
    dna_sequence = dna_sequence.upper()
    revc_sequence = revc(dna_sequence)
    sequences = [None]*6
    n = len(dna_sequence)//3
    r = len(dna_sequence)%3
    for i in range(3):
        if r == 2:
            sequences[i] = dna_sequence[i:3*n+i]
            sequences[3+i] = revc_sequence[i:3*n+i]
        elif r == 1:
            if i !=2 :
                sequences[i] = dna_sequence[i:3*n+i]
                sequences[3+i] = revc_sequence[i:3*n+i]
            else:
                sequences[i] = dna_sequence[2:3*n-1]
                sequences[3+i] = revc_sequence[2:3*n-1]
        else:
            if i != 0:
                sequences[i] = dna_sequence[i:3*n+i-3]
                sequences[3+i] = revc_sequence[i:3*n+i-3]
            else:
                sequences[i] = dna_sequence[0:3*n]
                sequences[3+i] = revc_sequence[0:3*n]

    return sequences

if __name__ == '__main__':
    totorf = 0
    for seq_name , seq in read_fasta("yeast_genome.fasta"):
        all_ori = get_orientations(seq)
        print(seq_name)
        for ori in all_ori:
           totorf += len(ret_ORF(ori))
    print(totorf)
