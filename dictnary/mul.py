dist = {'m1':4,'m2':3,'m3':4}
ans = 1
for key in dist:
    ans *= dist[key]

print(ans)