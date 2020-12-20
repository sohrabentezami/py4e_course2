fname = input('Enter the file name: ')
fhand = open(fname)

counts = dict()

for line in fhand :
    line = line.rstrip()
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1

lst = list()
for key,val in counts.items() :
    newtup = (val,key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val,key in lst[:15] :
    print(key,val)
