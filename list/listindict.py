students = [
    {"name":"Hitee","score":89},
    {"name":"Mihu","score":99},
    {"name":"Mishu","score":91},
    {"name":"Vency","score":85}
]

#built-in sorted() function already contains a loop inside it.
#passed entire list therefore it would loop through entire list from 0
#key would cotain score value from 0 to end
sort_marks_dec = sorted(students, key = lambda x:x['score'],reverse={True})

print(sort_marks_dec)

for x in sort_marks_dec:
    print(x)