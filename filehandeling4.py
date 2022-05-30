# file handeling

with open('read1.txt','rb') as f:
    n = int(input())
    data = f.readlines()[-n:]
    f.seek(5,1)
    a = f.tell()
    print(data)
    print(a)
f.close()
