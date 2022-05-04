disease_dictionary = {
    1: 'A',
    2: 'T', 3: 'G',
    4: 'C', 5: 'T', 6: 'A'
}
sample_sequence = "ATGCTA"
for snp in disease_dictionary:
    for idx, nucleotide in enumerate(sample_sequence):
        idx_scaled = idx + 1
        if snp == idx_scaled:
            if disease_dictionary[snp] == nucleotide:
                if idx_scaled == 1:
                    disease_exp = 'There is a point mutation at position 1 that is known to cause Cystic Fibrosis'
                if idx_scaled == 2:
                        disease_exp = 'There is a point mutation at position 2 that is known to cause ___'
                if idx_scaled == 3:
                        disease_exp = 'There is a point mutation at position 2 that is known to cause ___'
                if idx_scaled == 4:
                        disease_exp = 'There is a point mutation at position 2 that is known to cause ___'
                if idx_scaled == 5:
                        disease_exp = 'There is a point mutation at position 2 that is known to cause ___'
                if idx_scaled == 6:
                        disease_exp = 'There is a point mutation at position 2 that is known to cause ___'
                print(disease_exp)
