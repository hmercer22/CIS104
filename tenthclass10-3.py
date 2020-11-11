import string
name = input ("enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)

average = 0
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word :
            average += 1
            if letter not in counts:
                counts[letter] = 1
            else:
                counts[letter] += 1

lst = list()

for key,val in list(counts.items()):
    lst.append((val/average, key))

lst.sort(reverse=True)

for key, val in lst:
    print(key, val)
