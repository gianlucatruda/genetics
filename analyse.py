# Gianluca Truda
# 23 Feb 2016

name = input("Enter file name: ")
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

print("Pyrimidines:", counts['C']+ counts['T'])
print("Purines:", counts['A']+ counts['G'])
