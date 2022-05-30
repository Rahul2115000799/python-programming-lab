def max_no(a,b,c):
    max1=0
    if a>b and a>c:
        max1=a
    elif b>a and b>c:
        max1=b
    else:
        max1=c
    return max1
a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
c=int(input("Enter third no. : "))
print(max_no(a,b,c))
