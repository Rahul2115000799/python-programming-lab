# file handeling
# read no. of lines

with open ('read.txt') as f:
    ls = f.readlines()
    print(len(ls))
f.close()
