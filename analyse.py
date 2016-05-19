# Gianluca Truda
# 25 Feb 2016

import sys

#if sys.argv[0]:	
name = sys.argv[0]
#else:
#	name = input("Enter filename: ")

file = open(name, 'r', encoding = 'utf-8')

inStr = file.read()

counts = {'A':0,'C':0,'G':0,'T':0}

for i in range(len(inStr)):
    if inStr[i] == "A" or inStr[i] == "C" or inStr[i] == "G" or inStr[i] == "T":
        counts[inStr[i]] += 1
    
total = counts['A'] + counts['C'] + counts['G'] + counts['T']
print("\n\n",
      "C:",counts['C'], ":", round(counts['C']*100/total, 2),"%", "\n",
      "G:",counts['G'], ":", round(counts['G']*100/total, 2),"%", "\n", 
      "A:",counts['A'], ":", round(counts['A']*100/total, 2),"%", "\n",
      "T:",counts['T'], ":", round(counts['T']*100/total, 2),"%", "\n\n", 
      "Total:", total)

print("Pyrimidines:\t", counts['C']+ counts['T'])
print("Purines:\t", counts['A']+ counts['G'])
print("pyr/pur:\t",round((counts['C']+counts['T'])/(counts['A']+ counts['G']),3)) 
