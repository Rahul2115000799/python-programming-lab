# list in python 
# even number from a list



lst = list(map(int,input().split()))
for i in lst:
    if i % 2 == 0:
        print(i,end=' ')
