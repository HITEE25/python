def minimum(tpl):
    min = tpl[0]
    for x in tpl:
        if x < min:
            min = x
    return min

def maxi(tpl):
    max = tpl[0]
    for x in tpl:
        if x > max:
            max = x
    return max

def sum(tpl):
    sum = 0
    for x in tpl:
        sum += x
    return sum

tpl = (2,3,4,1)
print(f"min {minimum(tpl)}")
print(f"max {maxi(tpl)}")
print(f"sum {sum(tpl)}")
