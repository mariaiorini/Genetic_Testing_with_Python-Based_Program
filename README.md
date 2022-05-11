# Genetic testing with Python-based programs
## Using Python to detect SNPs in DNA sequences as well as the likelihood to develop Huntington's Disease
### Summary
This is a python code to identify mutations in a DNA sequence. The code has a directory which identifies the location of bases which have been identified to be associated with certain diseases. For example, a base "A" found at location 47 is associated with Cystic Fibrosis. The code runs through the DNA as an index and runs as a for loop to detect several different mutations. 
The code also checks for Huntington's disease, which is a repeat expansion disease. The code scans through the DNA sequence, looking at repeating triplets. If the triplet 'CAG' is found, then there is a chance of the individual having Huntington's disease. The number of CAG triplets is counted, and from that, a probability of developing the disease is displayed.
