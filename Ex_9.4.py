fname = input('Enter a file name: ')
fhand = open(fname)
counts = dict()

for line in fhand :
    line = line.rstrip()
    if line.startswith('From ') :
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1

bigcount = None
bigword = None

for x,y in counts.items() :
    if bigcount is None or y > bigcount :
        bigword = x
        bigcount = y

print(bigword, bigcount)
