#Hannah Mercer and Logan Yeubanks 11-17-2020

import re

name = input ("enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)

count = 0
rev = 0

for line in fhand:
    line = line.rstrip()
    if re.findall('New Revision: 3*', line):
        num = line[14:19]
        count += 1
        rev = rev + float(num)

avg = rev/count
print("Average", int(avg))
