d1 = {i:i**2 for i in range(1,6)}
d2 = {i:i**2 for i in range(6,11)}
'''d1 → main dictionary (gets changed)
d2 → dictionary whose data is added to d1
update() → merges dictionarie'''
d1.update(d2)
print(d1)