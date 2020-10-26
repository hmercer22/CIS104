fname = input ('Enter file name: ')
try :
    fhand = open(fname)
except :
    print(fname, 'file cannot be opened:')
    quit()
count = 0
tot = 0
ans = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    num = float(line[21:])
    tot = num + tot
ans = tot/count
print ("Average spam confidence:", ans)
