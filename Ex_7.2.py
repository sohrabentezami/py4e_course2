fname= input('Enter the file name: ')
fhand = open(fname)

x = 0
count = 0
value = 0

for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        ipos = line.find(':')
        piece = line[ipos+1:]
        value = float(piece)
        count = count + 1
        x = x + value

print('Average spam confidence: ', x/count)
