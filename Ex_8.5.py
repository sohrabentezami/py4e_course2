fname = input('Enter the file name: ')
fhand = open(fname)
count = 0

for line in fhand :
    line = line.rstrip()
    if line.startswith('From ') :
        etc = line.split()
        print(etc[1])
        count = count + 1

print(count)        
