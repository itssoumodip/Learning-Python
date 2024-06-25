# ## READING A FILE - >
# f = open('myfile2.txt', 'w')  ## r mode is default  ##for create write w
# # print(f)
# text = f.read()
# print(text)
# f.close()

# ## WRITE A FILE - >
# f = open("myfile_3.txt", 'w')
# f.write("Hello World")
# f.close()

# ## APPEND A FILE - >
# f = open("myfile_3.txt", 'a')
# f.write("Hello World ")
# f.close()

# ## WITHOUT CLOSING (SHORTCUT)
with open('myfile.txt', 'a') as f:
    f.write("Hello this a Try ")