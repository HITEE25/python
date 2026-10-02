s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("Not Anagram")
else:
    #created array to store frequency
    count = [0] * 256

    for ch in s1:
        count[ord(ch)] += 1#add the frequency for particular assci value

    for ch in s2:
        count[ord(ch)] -= 1#remove the frequency for particular assci value

    for i in count:
        if i != 0:
            print("Not Anagram")
            break
    else:
        print("Anagram")
