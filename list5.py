lst = list(input().split())
a = len(lst)
for i in range(0,a):
    temp=lst[0]
    lst[0]=lst[a-1]
    lst[a-1]=temp
print("New list is:")
print(lst)	
