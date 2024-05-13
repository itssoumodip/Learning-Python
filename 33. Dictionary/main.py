# Dicnary Example
dic = {
    "Name" : "Soumodip",      # KEY: VALUE
    "Degree" : "BCA",
    "Collge" : "Iem",
    1:"rohan",
    2:"sourav",
    3:"josi"
}
# TO PRINT PERTUCULAR VALUE [METHOD 1] ->
print(dic["Name"])  #DIC[KEY]   ## this case if not get the dicnory thorow Error
print(dic["Collge"])
print(dic[1])
print(dic[2])
print()

# PRINTING METHOD 2 ->
print(dic.get('Name'))
print(dic.get(5))         ## this case if not get the dicnory thorow None
print()

# TO PRINT FULL DICNORY - 
print(dic)
print()

# TO print all the keys
print(dic.keys())
    #  or    
for key in dic.keys():
    print(dic[key])

# TO print all the Values
print(dic.values())

# with F string - 
for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")
print()

## 
print(dic.items())
for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")
 