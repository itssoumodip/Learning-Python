names = "Soumodip,Rohan"
name = "ALU"

print(len(name))    # For count leangth - len()
print(len(names)) 
# For print like a loop 0 to 10 characters
print(names[0:10])  # <-{same}->  print(names[:10])  DEFAUL O TAKE  # INCLUDING 0 BUT NOT 4
# For print like a loop 2 to 10 characters
print(names[3:8])

print(names[:]) # PRINT THE HOOL

print(names[0:len(names)-3])    # SAME MEANING v
print(names[0:-3])              # SAME MEANING ^

print(names[len(names)-3:len(names)-1]) # SAME MEANING v
print(names[-3:-1])                     # SAME MEANING ^

# Quick Quiz
nm = "Harry"
print(nm[-4:-2])
