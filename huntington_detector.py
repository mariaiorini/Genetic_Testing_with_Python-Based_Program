def huntingtons_detector(huntFile_name): #input the name of desired file as string, ex: "huntington_2.fa"
    hunt_file = open(huntFile_name, "r")
    hunt_data = hunt_file.readlines()
    hunt_file.close()
    exon_1 = (hunt_data[2:8])
    exon_1 = "".join([str(elem) for elem in exon_1])
    exon_1 = "".join(exon_1.splitlines())
    exon_1 = "".join([line.strip() for line in exon_1])
    start = 0
    stop = 3
    hunt_counter = 0
    x = (len(exon_1)/3)
    while x >= 0:
        if exon_1[start:stop] == 'CAG':
            hunt_counter += 1
        start += 3
        stop += 3
        x -= 1
    if hunt_counter <= 26:
        result = "Normal: No risk of Disease."
    elif 27 <= hunt_counter <= 39:
        result = "Intermediate Risk: Not at risk, but potential to pass risk on to children."
    elif hunt_counter >= 40 :
        result = "Affected: Very likely to develop symptoms of HD."
    print("Number of CAG repeats:",hunt_counter)
    print(result)
    return(result)


