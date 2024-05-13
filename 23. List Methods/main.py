mylist = [1, 2, 3, 4]
mylist_2 = [1, 2, 3, 4]
# Use append ->
print(mylist)
mylist.append(7)
mylist.append(0)
mylist.append(16)
print(mylist)

# For Sorting ->
#   ASSENDING -->
mylist.sort()  
print(mylist)
#   DESSENDING -->
mylist.sort(reverse=True)
print(mylist)
  
# For reverse the string ->
mylist.reverse
print

# For print as a Index ->
print(mylist_2.index(1))
print(mylist_2)

# For Counting any no. in List
mylist_3 = [1,2,2,1,1,1,24]
print(mylist_3.count(1))

# For copy ->
'''
# Dont do like this
print(mylist)
newlist = mylist
newlist[0] = 0
print(mylist)
'''
# With Copy write this -
print(mylist)
newlist = mylist.copy
print(mylist)

# With Insert we can add anything in the list at any index we want - 
mylist.insert(1,192)  # means - (INDEX, Number)
print(mylist)

# For Extend (with this the no of the list go to the another list and append at the end)
oklist = [899893, 3298384, 43489948, 44344]
mylist.append(oklist)
print(oklist)
print(mylist)

# TO concatente we can do like this 
a1 = [1, 2, 3, 4, 5]
b1 = [93.5, 43.3, 44, 23.3]
c1 = a1+b1
print(c1)