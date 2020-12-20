fname = input('Enter the file name: ')
fhand = open(fname)

counts = dict()

for line in fhand :
    line = line.rstrip()
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1

print( sorted([(v,k) for k,v in counts.items()]))
