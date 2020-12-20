fname = input('Enter a file name: ')
fhand = open(fname)
counts = dict()

for line in fhand :
    line = line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        abc = words[1].split('@')
        counts[abc[1]] = counts.get(abc[1], 0) + 1

for x,y in counts.items() :
    print(x , y)

print(counts.items())
