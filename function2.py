def no_of_digits(n):
   c=0
   while n>0:
       c=c+1
       n=n//10
   return c
n=int(input("enter the number"))
c=n
s=0
while n>0:
   r=n%10
   s=s+r**(no_of_digits(c))
   n=n//10
if s==c:
   print("Number is armstrong")
else:
   print("Number is not armstrong")
