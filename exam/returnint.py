
def return_only_int(lst):
    result = []

    for item in lst:
        if type(item) == int:
            result.append(item)

    return result

print(return_only_int([45,"Hitee","hey",66,3,8,2]))