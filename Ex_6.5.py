str = 'X-DSPAM-Confidence:0.8475'

atpos = str.find('0')
char = str[atpos:]
number = float(char)
print(number)
