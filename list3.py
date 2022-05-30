# list in python
# odd numbers from a list

lst = list(map(int,input().split()))
for i in lst:
    if i % 2 != 0:
        print(i,end=' ')
