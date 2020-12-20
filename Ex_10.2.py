fname = input('Enter the file name: ')
fhand = open(fname)
counts = dict()

for line in fhand :
    line = line.rstrip()
    if line.startswith('From ') :
            words = line.split()
            etc = words[5]
            hr = etc.split(':')
            counts[hr[0]] = counts.get(hr[0],0) + 1

lst = list()
for key,val in counts.items() :
    newtup = (key,val)
    lst.append(newtup)

lst = sorted(lst)
for key,val in lst :
    print(key,val)
