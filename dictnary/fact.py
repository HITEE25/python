def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)

dist = {}
n = int(input("Enter size: "))

#it would start from 0
for i in range(n):
    key = i + 1
    dist[key] = fact(key)

print(dist)

