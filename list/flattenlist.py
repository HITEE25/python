'''Write a function that takes a nested list and flattens it into 
a single list. Print the original and flattened lists.'''

def flatten(list):
    #sublist contains [1,2,3]...,[7,8,9]
    #item contain item from sublist 1,2,3
    flat_list = [item for sublist in list for item in sublist]
    return flat_list

def flat_list(list):
    #took sublist from list
    flatten = []
    for sublist in list:
        #took item from sublist
        for item in sublist:
            flatten.append(item)
    return flatten

list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

flatten_list = flatten(list)
print(list)
print(flatten_list)

f = flat_list(list)
print(f)