# python pattern printing
# increasing char
# alphabet patterns

n = int(input("enter the number of rows"))
c = 65
for i in range(1,n+1):
    for j in range(i):
        print(chr(c),end=" ")
        c += 1
    print()
