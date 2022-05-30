# append in file

with open('read1.txt','a') as f:
    for i in range(4):
        name = input()
        f.write(name)
f.close()
print('data saved successfully')
