# python pattern printing
# increasing digits
# number patterns

n = int(input("enter the number of rows"))
c = 1
for i in range(1,n+1):
    for j in range(n+1-i):
        print(c,end="   ")
        c += 1
    print()
