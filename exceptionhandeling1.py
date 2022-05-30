a = 10
try:
    print(a/0)
except ZeroDivisionError:
    print('divide by 0')
