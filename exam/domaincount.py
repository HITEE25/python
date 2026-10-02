file = open("email.txt","r")
content = file.read()

domain_count = {}
for line in content:
    words = line.split()
    for word in words:
        if "@" in word:
            domain = word.split("@")[1]
            domain_count[domain] = domain_count.get(domain,0) + 1

print(domain_count)