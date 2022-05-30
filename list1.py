# canbalabce list
#list in python


c = 0
L = input("enter the elements of list = ")
l = L.split(" ")
sl = 0
for i in range(len(l)):
    sl = sl + int(l[i])
f = 0
for i in range(len(l)-1):
    f = f + int(l[i])
    sl = sl - int(l[i])
    if f == sl:
        c = c+1
        break
if c == 0:
    print("not balanced list")
else:
    print("balanced list")
    
