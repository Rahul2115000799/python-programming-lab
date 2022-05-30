# file handeling

f = open('read.txt','w')
n = int(input())
a = 0
while a<n:
    f.write(f'{a*a} is a square of {a}\n')
    a = a+1
    if a>n:
        break
f.close()
print('data saved successfully')
