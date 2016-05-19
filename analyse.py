# Gianluca Truda
# Original :	25 Feb 2016
# Updated :		19 May 2016

import sys

# Input control

if (len(sys.argv) == 2):
	if (sys.argv[1] != ""): name = sys.argv[1]
elif (len(sys.argv)>2):
	print("Error: too many arguments given!")
	sys.exit()
else:
	name = input("Enter filename: ")

# Variable initiation

counts = {'A':0,'C':0,'G':0,'T':0}
file = open(name, 'r', encoding = 'utf-8')
inStr = file.read()

# Reading from file

for i in range(len(inStr)):
    if inStr[i] == "A" or inStr[i] == "C" or inStr[i] == "G" or inStr[i] == "T":
        counts[inStr[i]] += 1
    

# Output of data

total = counts['A'] + counts['C'] + counts['G'] + counts['T']
print("\n\n",
      "C:",counts['C'], ":\t", round(counts['C']*100/total, 2),"%", "\n",
      "G:",counts['G'], ":\t", round(counts['G']*100/total, 2),"%", "\n", 
      "A:",counts['A'], ":\t", round(counts['A']*100/total, 2),"%", "\n",
      "T:",counts['T'], ":\t", round(counts['T']*100/total, 2),"%", "\n\n", 
      "Total:", total)

print("Pyrimidines:\t", counts['C']+ counts['T'])
print("Purines:\t", counts['A']+ counts['G'])
print("pyr/pur:\t",round((counts['C']+counts['T'])/(counts['A']+ counts['G']),3)) 

# Shutdown
sys.exit()

