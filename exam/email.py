file = open("email.txt", "r")
lines = file.readlines()

domain_count = {}

for line in lines:
    words = line.split()
    print(words)
    for word in words:
        print(word)
        if "@" in word:
            domain = word.split("@")[1]
            print(domain)
            domain_count[domain] = domain_count.get(domain, 0) + 1

print("Email domain count:", domain_count)

file.close()