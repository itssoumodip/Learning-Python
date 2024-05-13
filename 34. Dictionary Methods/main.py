ep_1 = {
    12: 32,
    234: 34,
    23: 24
}
ep_2 = {
    24: 43,
    90: 43,
    943: 543
}
# For update
ep_1.update(ep_2)
print(ep_1)

# For Clear 
ep_1.clear()
print(ep_1)

# For making Empty Dicnory
empty = {}
print(empty)

# For delete one key value in Dicnory - 
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

