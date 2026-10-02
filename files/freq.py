filename = input("Enter filname")
file = open(filename,'r')
data = file.read()

freq = {}
for ch in data:
    if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z':
        ch = ch.lower()
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

print("histogram")
for key in freq:
    #how many times repeated freq[key]
    print(key,":","*"*freq[key])