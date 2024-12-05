#Funciones incorporadas

num  = [ 13,2.4, 12, 4.3, 6.1, 8, 10, 11.1]

#print( num[0] + num[1] + num[2] + num[3] + num[4] + num[5])

#print(sum(num))

max = num[1]
for i in num:
    if i > max:
        max = i
        print(max)
print(max)

