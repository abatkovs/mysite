n = ''
name = 'Thé Fàllén Angél'
if(len(name)> 1):
    for i in name:
        n = n + " " + i
else:
    n = name[0]
print('User input: ', n)