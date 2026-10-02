def unique(L):
    result = []
    for i in L:
        if i not in result:
            result.append(i)
    return sorted(result)

def uni(L):
    return list(set(L))

L = [4,6,6,7,1,2,2,3]
print(unique(L))
print(uni(L))