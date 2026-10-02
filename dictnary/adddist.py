d1 = {"name":"hitee","id":12,"gender":"female"}
d2 = {"name":"mihu","id":14}
d = {}

for key in d1:
    if key in d2:
        d[key] = d1[key] + d2[key]

print(d)
