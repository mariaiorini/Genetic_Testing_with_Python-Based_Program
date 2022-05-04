

# In this case, I pick a gene and store all of its
# assoicated SNPs in a dictornary like below.
# The integer (Key) represents to position the
# SNP is on the gene, and the letter represents
# the SNP.
disease_dictionary = {
    1:'A' , 3:'T' , 4:'G',
    5:'C' , 6:'T' , 10:'A'
}


# Here, I made up a sample sequence, but you could read this in
# using a fasta files instead of an inserted string.
sample_sequence = ("ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGC"
"TATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAAC"
"CTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAA"
"CTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGA"
"TATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTAGTCAACTTGTTG"
"AAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAG"
"TATGCAAACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACA"
"TCTAAAAGATGAAGTTTCTATCATCCAAAGTATGGGCTACAGAAACCGTG"
"CCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAAACC"
"AGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGAC"
"AAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGAT"
"CTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGA"
"GATCAAGAATTGTTACAAATCACCCCTCAAGGAACCAGGGATGAAATCAG"
"TTTGGATTCTGCAAAAAAGGCTGCTTGTGAATTTTCTGAGACGGATGTAA"
"CAAATACTGAACATCATCAACCCAGTAATAATGATTTGAACACCACTGAG"
"AAGCGTGCAGCTGAGAGGCATCCAGAAAAGTATCAGGGTGAAGCAGCATC"
"TGGGTGTGAGAGTGAAACAAGCGTCTCTGAAGACTGCTCAGGGCTATCCT"
"CTCAGAGTGACATTTTAACCACTCAGCAGAGGGATACCATGCAACATAAC"
"CTGATAAAGCTCCAGCAGGAAATGGCTGAACTAGAAGCTGTGTTAGAACA"
"GCATGGGAGCCAGCCTTCTAACAGCTACCCTTCCATCATAAGTGACTCTT"
"CTGCCCTTGAGGACCTGCGAAATCCAGAACAAAGCACATCAGAAAAAGTA"
"TTAACTTCACAGAAAAGTAGTGAATACCCTATAAGCCAGAATCCAGAAGG"
"CCTTTCTGCTGACAAGTTTGAGGTGTCTGCAGATAGTTCTACCAGTAAAA"
"ATAAAGAACCAGGAGTGGAAAGGTCATCCCCTTCTAAATGCCCATCATTA"
"GATGATAGGTGGTACATGCACAGTTGCTCTGGGAGTCTTCAGAATAGAAA"
"CTACCCATCTCAAGAGGAGCTCATTAAGGTTGTTGATGTGGAGGAGCAAC"
"AGCTGGAAGAGTCTGGGCCACACGATTTGACGGAAACATCTTACTTGCCA"
"AGGCAAGATCTAGAGGGAACCCCTTACCTGGAATCTGGAATCAGCCTCTT"
"CTCTGATGACCCTGAATCTGATCCTTCTGAAGACAGAGCCCCAGAGTCAG"
"CTCGTGTTGGCAACATACCATCTTCAACCTCTGCATTGAAAGTTCCCCAA"
"TTGAAAGTTGCAGAATCTGCCCAGAGTCCAGCTGCTGCTCATACTACTGA"
"TACTGCTGGGTATAATGCAATGGAAGAAAGTGTGAGCAGGGAGAAGCCAG"
"AATTGACAGCTTCAACAGAAAGGGTCAACAAAAGAATGTCCATGGTGGTG"
"TCTGGCCTGACCCCAGAAGAATTTATGCTCGTGTACAAGTTTGCCAGAAA"
"ACACCACATCACTTTAACTAATCTAATTACTGAAGAGACTACTCATGTTG"
"TTATGAAAACAGATGCTGAGTTTGTGTGTGAACGGACACTGAAATATTTT"
"CTAGGAATTGCGGGAGGAAAATGGGTAGTTAGCTATTTCTGGGTGACCCA"
"GTCTATTAAAGAAAGAAAAATGCTGAATGAGCATGATTTTGAAGTCAGAG"
"GAGATGTGGTCAATGGAAGAAACCACCAAGGTCCAAAGCGAGCAAGAGAA"
"TCCCAGGACAGAAAGATCTTCAGGGGGCTAGAAATCTGTTGCTATGGGCC"
"CTTCACCAACATGCCCACAGATCAACTGGAATGGATGGTACAGCTGTGTG"
"GTGCTTCTGTGGTGAAGGAGCTTTCATCATTCACCCTTGGCACAGGTGTC"
"CACCCAATTGTGGTTGTGCAGCCAGATGCCTGGACAGAGGACAATGGCTT"
"CCATGCAATTGGGCAGATGTGTGAGGCACCTGTGGTGACCCGAGAGTGGG"
"TGTTGGACAGTGTAGCACTCTACCAGTGCCAGGAGCTGGACACCTACCTG"
"ATACCCCAGATCCCCCACAGCCACTACTGA")


# Similar to above, I am going through the entire SNP library first (line 60).
# Then, I am going to go through the entire sample sequence (line 61).
# Additionally, I used the enumerate function to be able
# to store the index of every letter in the sequence (line 61).
# I also added "1" to the index before determining whether
# they match anything in the dictionary because computers
# start counting beginning with zero vs. one (line 62). Then, I
# determined if the position of the sequence matched the position of
# the SNP (line 63). If the SNP matches the nucleotide at that position (line 64),
# then, the nucleotide and scaled position will be printed (line 65).
detected_snps = []
for snp in disease_dictionary:
    for idx,nucleotide in enumerate(sample_sequence):
        idx_scaled = idx + 1
        if snp == idx_scaled:
            if disease_dictionary[snp] == nucleotide:
                print(nucleotide, idx_scaled)
                detected_snps.append(idx_scaled)
                print(detected_snps)
# You could check the sequences with output and they should match.