L = (10,20,30,40,50)

print(L[0])
print(L[-1])

print(L[1:4])

print(len(L))

L = L + (60,)
print(L)

y = L[0:2]
y = y + (99,)
L = y + L[3:5]
print(L)


