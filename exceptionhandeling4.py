print('start')
lst = ['a','b']
try:
    out = lst[2]
    print(out)
except:
    print('Ivalid Index')
finally:
    print('stop')
