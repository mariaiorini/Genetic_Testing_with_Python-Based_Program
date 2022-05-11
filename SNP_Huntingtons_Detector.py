def SNP_Huntingtons_Detector(seq_fileName):  # must input the name of desired file as string, ex: "seqData_2.fa"

    seq_file = open(seq_fileName, "r")
    seq_data = seq_file.read()
    seq_file.close()
    seq_data = seq_data.splitlines()
    seq_data = seq_data[1:]
    seq_data = "".join([str(elem) for elem in seq_data])
    seq_data = "".join([line.strip() for line in seq_data])
    start_codon = seq_data.index("TAC")
    seq_data = seq_data[start_codon:]
    print(seq_data)


    disease_dictionary = {
        47: 'A',
        3000: 'T', 4679: 'G',
        5012: 'C', 8403: 'T', 11439: 'A'
    }
#create dt with no disease, create one with multiple

    detected_snps = []
    for snp in disease_dictionary:
        for idx, nucleotide in enumerate(seq_data):
            idx_scaled = idx + 1
            if snp == idx_scaled:
                if disease_dictionary[snp] == nucleotide:
                    if idx_scaled == 47:
                        disease_exp = ' There is a point mutation at position 47 that is known to contribute to Cystic Fibrosis.'
                        detected_snps.append(disease_exp)
                    if idx_scaled == 3000:
                        disease_exp = ' There is a point mutation at position 3000 that is known to contribute to Schizophrenia'
                        detected_snps.append(disease_exp)
                    if idx_scaled == 4679:
                        disease_exp = ' There is a point mutation at position 4679 that is known to contribute to Alzheimers.'
                        detected_snps.append(disease_exp)
                    if idx_scaled == 5012:
                        disease_exp = ' There is a point mutation at position 5012 that is known to contribute to Breast Cancer.'
                        detected_snps.append(disease_exp)
                    if idx_scaled == 8403:
                        disease_exp = ' There is a point mutation at position 8403 that is known to contribute to Rheumatoid Arthritis.'
                        detected_snps.append(disease_exp)
                    if idx_scaled == 11439:
                        disease_exp = 'There is a point mutation at position 11439 that is known to contribute to Obesity.'
                        detected_snps.append(disease_exp)
                    else:
                        disease_exp = ''
                        detected_snps.append(disease_exp)

    if bool(detected_snps)== False:
        disease_exp = "There are no point mutation known to cause disease."
        detected_snps.append(disease_exp)





    seq_data = seq_data[1999:2999]
    start = 0
    stop = 3
    hunt_counter = 0
    countdown = (len(seq_data) / 3)
    while countdown >= 0:
        if seq_data[start:stop] == 'CAG':
            hunt_counter += 1
        start += 3
        stop += 3
        countdown -= 1
    if hunt_counter <= 26:
        hunt_result = "Number of CAG repeats: " + str(hunt_counter) + \
                      "\nHuntington's Likelihood: No risk of disease."
    elif 27 <= hunt_counter <= 35:
        hunt_result = "Number of CAG repeats: " + str(hunt_counter) + \
                      "\nHuntington's Likelihood:  Not at risk of developing symptoms of HD but " \
                      "may be at risk of having a child with CAG repeats in the HD-causing range."
    elif 36 <= hunt_counter <= 39:
        hunt_result = "Number of CAG repeats: " + str(hunt_counter) + \
                      "\nHuntington's Likelihood: May or may not develop symptoms of HD " \
                      "and future generations could be at risk."
    elif hunt_counter >= 40:
        hunt_result = "Number of CAG repeats: " + str(hunt_counter) + \
                      "\nHuntington's Likelihood: Will develop symptoms of HD over a natural lifetime." \

    detected_snps = "".join([str(elem) for elem in detected_snps])

    import tkinter as tk
    from tkinter import ttk

    popup = tk.Tk()
    popup.wm_title("Test Results")
    label = ttk.Label(popup, text=detected_snps+"\n"+hunt_result, font="NORM_FONT")
    label.pack(side="top", fill="x", pady=10)
    b1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    b1.pack()
    popup.mainloop()

    return(hunt_result,detected_snps)
