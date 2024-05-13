s1 = {1,2,3,4}
s2 = {4,5,6}
# For Union -
print(s1.union(s2))
print(s1,s2)
print()

#  For Update (means - in s1 insert s2 elements)
s1.update(s2)
print(s1,s2)
print()

# For Intersection -
print(s1.intersection(s2))
print()

# For Intersection Update - 
s1.intersection_update(s2)
print(s1,s2)
print()

# For Symetric Difference - (don't common)
l1 = {1,2,3,4,5}
l2 = {5,6,7,8}
print(l1.symmetric_difference(l2))
print()

# For Symetric Difference Update (For update the symetric differcene )

# For Difference (present in set1 but not present set2)
print(l1.difference(l2))
print()

# For Difference Update (present in set1 but not present set2)
print(l1.difference(l2))
print()

# DisJoint set (The isdisjoint() method checks if items of given set are present in another set.)
sl1 = {"Ami", "Holam", "Romio"}
sl2 = {"Lady", "killer", "Romio"}
print(sl1.isdisjoint(sl2))
print()

# Super ser (The issuperset() method checks if all the items of a particular set are present in the original set. )
sl_1 = {1,2,3,4,5,6}
sl_2 = {2,4,5}
print(sl_1.issuperset(sl_2))
print()

# Subset (The issubset() method checks if all the items of the original set are present in the particular set.)
sb1 = {1,2,3,4,5,6}
sb2 = {3,5}
print(sb2.issubset(sb1))
print()

# For add (If you want to add a single item to the set use the add() method.)
ad = {1,2,3,4,5}
print(ad)
ad.add(6)
print(ad)
print()

# For update (If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.)
up1 = {1,2,3,4,5}
up2 = {6,7,8,9,10}
print(up1)
up1.update(up2)
print(up1)
print()

# remove()/discard() - We can use remove() and discard() methods to remove items form list.
dis = {1,2,4,5}
dis.remove(2)     #with remove
print(dis)
dis.discard(1)    #with discard 
print(dis)
print()

# pop()
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
pp = {1,2,3,4}
pp2 = pp.pop()
print(pp)
print(pp2)
print()

# For del (del is not a method, rather it is a keyword which deletes the set entirely.)
d = {1,2,3,4,5}
print(d)
# del d   (delete - error)
print(d)
print()

# clear(): This method clears all items in the set and prints an empty set.
c = {1,23,4,5,6}
print(c)
c.clear()
print(c)  #empty set
print()

# set with if else ->
con = {1,2,3,4,5,6}
if 1 in con:
    print("1 is in the set")
else:
    print("Not present !!")