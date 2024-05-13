# We can do this
'''
letter = "My name is {} and i am from {}"
print(letter)
name = "Soumodip"
place = "Kolkata"
print(letter.format(name, place))
'''
# OR We can do this 
'''
letter = "My name is {1} and i am from {0}"
print(letter)
name = "Soumodip"
place = "Kolkata"
print(letter.format(place, name))
'''
# F-STRING ->
name = "Soumodip"
place = "Kolkata"
print(f"Hello my name is {name} and i am from {place}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# F-STRING ->
p = 23.99990
txt_2 = f"For only {p:.2f} dollars!!"
print(txt_2)
