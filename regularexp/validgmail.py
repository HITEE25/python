import re

gmails = ["hitee@gmail.com","hitee.com"]
#\w words 
#+ one or more
# \. to pint real dot because . repersent any char
for email in gmails:
    if re.match(r'^\w+@gmail\.com',email):
        print(email)