# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

# marks = [1,2,3,45,6,6,77,77,43,33]
# index = 0
# for mark in marks:
#     print(mark) 
#     if index == 3:
#         print("Soumodip")
#     index += 1

## METHOD IS -
marks = [0,3,2,4,5,6,3,2,3,4,5,3]
for index, mark in enumerate(marks):
    print(mark)
    if (index==3):
        print("Harry, awesome")