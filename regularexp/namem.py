import re

names = ["Ramsesh","Ram","Suresh","Ritesh","hitee"]

pattern = r'^[RSrs].*[HJhj]$'

for name in names:
    if re.match(pattern,name):
        print(name)