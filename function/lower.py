def count_case(str):
    count_l = 0
    count_u = 0

    for ch in str:
        if ch >= 'a' and ch <= 'z':
            count_l += 1
        if ch >= 'A' and ch <= 'Z':
            count_u += 1

    print("Lower:",count_l)
    print("Upper:",count_u)

str=input("Enter string:")
count_case(str)