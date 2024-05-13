"""
Manipulating Tuples - 
Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.
"""
'''
o_tup = ('Soumodip', 'Animesh', 'Hello', 'Helechi')
print("Original Tupple -", o_tup)
o_tup_to_list_convert = list(o_tup)   # to convert tupple to list
o_tup_to_list_convert.append('Pakistan')   # add item
print("add item in Tupple (APPEND)-", o_tup_to_list_convert)
o_tup_to_list_convert.pop(1)                # remove item
print("remove item in Tupple (REMOVE 1) -", o_tup_to_list_convert)
o_tup_to_list_convert[2]='String'           # change item
print("change item in Original Tupple (CHANGE 2) -", o_tup_to_list_convert)
o_tup = tuple(o_tup_to_list_convert)     # list to convert to tupple 
print("Original Tupple -", o_tup)
'''
'''
# TO concatinate 2 Tupple - 
t_1 = ('sinechan', 'doremon', 'hatori')
t_2 = ('anime', 'laptop')
t_3 = t_1 + t_2
print(t_3)
print(t_2)
print(t_1)
'''

# to count in Tupple
tot = (0,1,2,3,3,4,4,9,5,4,94,4,9,4,94,4,4)
print(tot.count(4))
tot_count = tot.count(4)
print(tot_count)

# The Index() method returns the first occurrence of the given element from the tuple.
tot_index = tot.index(4)

slice_and_find_index = tot.index(0, 14, 9) ## MEANING - from 8 index to 14 find 9, find 9 at what index
print(slice_and_find_index)