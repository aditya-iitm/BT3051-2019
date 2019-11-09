#BT3051 Assignment 1b
#Roll number : BS16B019
#Collaborators : None
#Time : 0:45

import sys
import doctest

def read_FASTA(fname):
	"""(str) -> (list of tuples)
		Reads a fasta file and returns a list of tuples containing
		the header and the sequence
	"""
	with open(fname) as f:
		data = f.readlines()
		sequences = []
		sequence,sequence_name = '',''
		
		#Iterate through values in data
		for line in data:
			#Check for header
			if line[0] == '>':
				#Append seqeunce_name,sequence as a tuple to the list if sequence is not empty
				if sequence != '' : sequences.append((sequence_name,sequence))
				sequence = ''						#Reinitialize sequence  
				sequence_name = line[1:].strip()	#Assign sequence_name
			#Store sequence corresponding to header
			else:
				sequence += line.strip()
		#Append last seqeunce_name,sequence as a tuple to the list
		sequences.append((sequence_name,sequence))
	#Return list of tuples
	return sequences

def identify_orfs(dna_sequence):
	"""(str) -> (list of str)
		Takes in each orientation as an input and returns Open Reading Frames,
		if there are none in the sequence, returns None
	"""
	dna_sequence = dna_sequence.upper()
	start = 'ATG'
	stop = ['TAG','TAA','TGA']
	#Initializing start index and end index, in case a sequence contains multiple ORFs
	starti,endi = [],[]
	ORF = []
	
	#Iterates through the length of the dna sequence
	for i in range(0,len(dna_sequence),3):
		if dna_sequence[i:i+3] == start : starti.append(i)	#Checks for the start codon to start appending, appends index to starti
		if dna_sequence[i:i+3] in stop  : endi.append(i+3) 	#Checks for the stop codon and appends the position to endi
	#Iterates through the number of start indices
	for i in range(len(starti)):
		for j in range(len(endi)):
			#Checks if start index is less than stop index (incase multiple ORFs are possible in a sequence),
			#and appends the ORF to a list
			if starti[i] < endi[j] :
				ORF.append(dna_sequence[starti[i] : endi[j]])
				break
	#If ORFs are present, return the ORF
	if ORF : return ORF
	return 'None'

def translate_DNA(dnaStrand):
	""" (str) -> (str)
		Takes in each ORF and translates it using the translational table
		Test case :
		>>> translate_DNA('ATGTATGATGCGACCGCGAGCACCCGCTGCACCCGCGAAAGCTGA')
		'MYDATASTRCTRES'
	"""
	protein = ''
	translation_table = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
	}
	#Iterates through sequence, one codon at a time
	for i in range(0,len(dnaStrand),3):
		#Looks up symbol using the dictionary
		symbol = translation_table[dnaStrand[i:i+3]]
		#ends tranlation if its a stop codon
		if symbol == 'Stop' : break
		protein += symbol
	#returns the translated protein
	return protein

def compute_protein_mass(protein_string):
	""" (str) -> (float)
		Computes the mass of the given protein sequence
		Test case :
		>>> compute_protein_mass('SKADYEK')
		821.392
	"""
	mass_table = {
	'A' :  71.03711,
	'C' :  103.00919,
	'D' :  115.02694,
	'E' :  129.04259,
	'F' :  147.06841,
	'G' :  57.02146,
	'H' :  137.05891,
	'I' :  113.08406,
	'K' :  128.09496,
	'L' :  113.08406,
	'M' :  131.04049,
	'N' :  114.04293,
	'P' :  97.05276,
	'Q' :  128.05858,
	'R' :  156.10111,
	'S' :  87.03203,
	'T' :  101.04768,
	'V' :  99.06841,
	'W' :  186.07931,
	'Y' :  163.06333 
	}
	mass = 0
	#Iterates through the protein sequence and adds mass after looking up 
	#each amino acid's mass in the dictionary
	for i in protein_string : mass += mass_table[i]
	return round(mass,3)

if __name__ == '__main__':
	#file = input("Enter file name : ")
	for seq_name, seq in read_FASTA("yeast_genome.fasta") : 
		print(seq_name+":")
		for orf in identify_orfs(seq):
			protein=translate_DNA(orf)
			print(protein, compute_protein_mass(protein))