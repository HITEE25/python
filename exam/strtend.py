import re

names = ["ramesh","mahesh","raj","mihu"]

pattern = r"^[R,S,r,s]\w*[H,J,h,j]$"

matched = []

for name in names:
    if re.match(pattern,name):
        matched.append(name)

print(matched)