#open the histogram.txt file
file = open("histogram.txt",'r')
data = file.read()

freq = {}

for ch in data:
    if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z':
        #covert to lower case because want to count both lower and upper case
        ch = ch.lower()
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

print("Histogram: ")

for key in freq:
    #key store char
    print(key,":","*"*freq[key])
file.close()

