# python pattern printing question
# inverted triangle
# star pattern 

n = int(input("enter the number of rows"))
for i in range(1,n+1):
    for j in range(n+1-i):
        print("*",end="")
    print()
