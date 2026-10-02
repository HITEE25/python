import re

contact = "contact no: 9783443678, 8167278934"
#replace with sub
#search with search
#find matching with match
#must start with 9 , \d should be digit ,{9} other 9 digit
result = re.sub(r'9\d{9}',"hidden",contact)
print(result)
