list_by_me = [0,1,2,3,4,5,6,7,8,9,10, "Hello", True]
"""
print(list_by_me)
print(list_by_me[0])
print(list_by_me[2])
print(list_by_me[3])
"""
'''
print(list_by_me[-3])                   # Negative Index
print(list_by_me[len(list_by_me)-3])    # Positive Index
'''
"""
# To Check whether an item in present in the list?
if 90 in list_by_me:                 # FOR INTEGER
    print("Yes Present")
else:
    print("Not Present")

if "Hello" in list_by_me:            # FOR STRING
    print("Yes Present")
else:
    print("Not Present")

if 'llo' in 'Hello':
    print("Yes Present")
else:
    print("Not Present")
"""
'''
print(list_by_me[:])
print(list_by_me[1:])
print(list_by_me[1:12:2])
'''
# List Comprehension
lst = [i for i in range(4)]
print(lst)
lst = [i*i for i in range(4)]
print(lst)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

