# Name- Pratyush Singh
# Programming Assignment #7


# This assignment focuses on lists and file/text processing.
# The assignment involves processing data from genome files.
# Our program works with the two given input files.

"""
constants
"""

MIN_CODONS = 5
MIN_CG = 30
UNIQUE_NUCLEOTIDES = 4
NUCLEOTIDES_CODONS = 3

"""
main: controler of program display summary of program
"""
def main():
    print("This program reports information about DNA nucleotide sequences that may encode proteins.")
    # take input file and output file name
    input_file = str(input("Input file name? "))
    output_file = str(input("Output file name? "))
    # read from input file
    file_lines = read_input(input_file)
    # do calculations and compute output
    output = compute_nucleotide_sequence(file_lines)
    # write to the output file name
    write_output(output,output_file)


"""
read data from file
"""
def read_input(input_file):
    # open file and get its handel
    in_file = open(input_file)
    # read all lines of the file
    file_lines = in_file.readlines()
    # close the file
    in_file.close()
    return file_lines

"""
computes the output and return result to the main
"""
def compute_nucleotide_sequence(file_lines):
    line_index = 0
    dump_in_file = []
    for line in file_lines:
        # strip end of lines from line
        line = line.strip()
        #perform computation on every second line of the file
        if((line_index % 2) != 0):
            total_mass = []
            dump_in_file.append(["Nucleotides: "+line.upper()])
            nuc_counts = [0] * (UNIQUE_NUCLEOTIDES + 1)
            mass_percentage = [0] * (UNIQUE_NUCLEOTIDES + 1)
            codons = []
            
            # get the count of each nucleotide
            compute_nucleotide_count(line , nuc_counts)
            # get the mass of each nucleotide
            compute_mass_percentage(nuc_counts, mass_percentage, total_mass)
            # get the list of codons
            compute_codons(codons,line)
            # test if the sequence qualifies as a protein
            isprotein = is_protein(codons,mass_percentage)
            # remove last for (-)
            # append every thing in a list to dump in a file
            nuc_counts.pop(4)
            dump_in_file.append(["Nuc. Counts: "+str(nuc_counts)])
            # remove last for (-)
            mass_percentage.pop(4)
            dump_in_file.append(["Total Mass%: "+str(mass_percentage)+" of "+str(total_mass[0])])
            dump_in_file.append(["Codons List: "+str(codons)])
            dump_in_file.append(["Is Protein?: "+str(isprotein)])
        else:
            dump_in_file.append(["Region Name: "+line]) # add first line in list
        line_index +=1
    return dump_in_file
        
"""
compute the count of each nucleotide
"""
def compute_nucleotide_count(line , nuc_counts):
    line = line.strip()
    for nucleotide in line:
        nucleotide = nucleotide.upper()
        if(nucleotide == 'A'):
            nuc_counts[0] +=1
        if(nucleotide == 'C'):
            nuc_counts[1] +=1
        if(nucleotide == 'G'):
            nuc_counts[2] +=1
        if(nucleotide == 'T'):
            nuc_counts[3] +=1
        if(nucleotide == '-'):
            nuc_counts[4] +=1


"""
 # compute mass percentage of each nucleotide
"""
def compute_mass_percentage(nuc_counts, mass_percentage, total_mass):
    nucleotide_mass = [135.128, 111.103, 151.128, 125.107, 100.000]
    total = 0
    # calculate the total mass
    for i in range(0, len(nuc_counts)):
        total += nucleotide_mass[i] * nuc_counts[i]
        
    total_mass.append(round(total, 1))
    
    # calculate mass percentage of each nucleotide
    for i in range(0, len(nuc_counts)):
        mass = ((nucleotide_mass[i] * nuc_counts[i])/total) * 100
        mass = round(mass, 1)
        mass_percentage[i] = mass


"""
# compute codons triplet of nucleotide
"""
def compute_codons(codons,line):
    line = line.strip()
    index = 0
    codon = []
    for nucleotide in line:
        nucleotide = nucleotide.strip()
        # skip the - as it is not required
        if(nucleotide == '-'):
            continue
        # add the last nucleotide in codons and create new list
        if(index == NUCLEOTIDES_CODONS-1):
            codon.append(nucleotide.upper())
            codons.append(list_to_string(codon))
            index = 0
            codon = []
        else:
            codon.append(nucleotide.upper())
            index +=1
        
"""
conversion from list to string
"""
def list_to_string(lists):
    string_ls = ''.join(lists)
    return string_ls
"""
evaluation of the sequence to qualify as a protein
"""
def is_protein(codons,mass_percentage):
    start_codon = "ATG"
    stop_codon = ["TAA", "TAG", "TGA"]
    
    if(codons[0] == start_codon and (codons[len(codons) -1 ] in stop_codon) and (len(codons) >=MIN_CODONS) and (mass_percentage[1] + mass_percentage[2]) >=MIN_CG):
        return "YES"
    else:
        return "NO"
"""
write data to the file
"""
def write_output(output, output_file):
# write each line in file
    with open(output_file, 'w') as f:
        for line in output:
            f.write('\n'+(list_to_string(line)))


main()
