#Translate sequence

from Bio import SeqIO
def translate_seq(sequence): #Start function
    records= list(SeqIO.parse(sequence, "fasta")) # Set up pour ouvrir le fasta
    sequence=records[0]
    introns=records[1:]
    new_RNAm_string=[] #New list
    for i in sequence: #Start loop sur la sequence du FASTA
        if i == 'T':
            new_RNAm_string.append('A') # 4x le pairing de chaque base
        elif i == 'A':
            new_RNAm_string.append('U')
        elif i == 'G':
            new_RNAm_string.append('C')
        elif i == 'C':
            new_RNAm_string.append('G')
        else:
            print("Please no")
            new_RNAm_string = None
            break
    try:
        return''.join(new_RNAm_string)
    except:
        pass
translateSeq=translate_seq("C:/Python_Files/Dev2_2.fasta")
print(translateSeq)

from Bio import SeqIO
def translate_introns(sequence): #Start function
    records= list(SeqIO.parse(sequence, "fasta")) # Set up pour ouvrir le fasta
    intron=records[1:]
    new_intron_strings=[] #New list
    for x in intron:
         for i in x: #Start loop sur la sequence du FASTA
            if i == 'T':
                new_intron_strings.append('U') # 4x le pairing de chaque base
            elif i == 'A':
                new_intron_strings.append('A')
            elif i == 'G':
                new_intron_strings.append('G')
            elif i == 'C':
                new_intron_strings.append('C')
            elif i == len(x):
                new_intron_strings.append(',')
            else:
                print("Please no")
                new_intron_strings = None
                break
    try:
        return''.join(new_intron_strings)
    except:
        pass
translateI=translate_introns("C:/Python_Files/Dev2_2.fasta")
print(translateI)

