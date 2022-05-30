n = int(input("enter the number : "))

sum = 0
temp = n
while temp > 0:
    dig = temp % 10
    sum += pow(dig,n)
    temp //= 10

if(n == sum):
    print("armstrong")

else:
    print("not armstrong")
