arr = [56,3,78,3,45,23]

n = len(arr)

for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]


print(arr)