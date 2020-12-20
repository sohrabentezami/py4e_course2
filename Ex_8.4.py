fname = input('Enter the file name: ')
fhand = open(fname)
x = list()

for line in fhand :
    line = line.rstrip()
    etc = line.split()
    for i in range(len(etc)) :
        if etc[i] not in x:
            x.append(etc[i])

x.sort()
print(x)
