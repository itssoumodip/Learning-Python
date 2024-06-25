# with open('file.txt','r') as f:
#     print(type(f))
#     # Move to the 10th byte in the file
#     f.seek(10)
#     ## Save a current position
#     current_possition = f.tell()
#     print(current_possition)
#     ## Read the next 5 bytes 
#     data=f.read(5)
#     print(data)

with open('sample.txt','w') as f:
    f.write('Hello World!')
    f.truncate(5)

with open('sample.txt', 'r') as f:
    print(f.read())