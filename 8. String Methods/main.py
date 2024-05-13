
# STRINGS ARE IMMUTABLE
x = "soumodip"
y = "SOUMODIP"
print(len(x))
# For Upper Case ->
print(x.upper())
# For Lower Case ->
print(y.lower())
# For RS Strip ->
a = "!! SOUMO !!!!!!!!!!!!!!!!!!!"
print(a.rstrip("!")) # after word NOT before
print(a)
# For Replace any Word ->
print(a.replace("!","$"))
# For Split ->
print(a.split(" "))
# For Capitalize ->
blogHeading = "introduction to js"
print(blogHeading.capitalize())
# For Center ->
print(blogHeading.center(50))
print(len(blogHeading.center(50)))
# For Count any word ->
c = "Soumodip ---------- Soumodip !!!!!!!!! Soumodip"
print(c.count("Soumodip"))
# For Endswith (like a Condition to check in the END)      #return Boolen type
print(a.endswith("!!"))
# For Startsswith (like a Condition to check in the START)      #return Boolen type
print(a.startswith("!!"))
# For check the last with the array ->
print(c.endswith("---", 9,11))
# For find ->
print(x.find("dip"))
# For Index -> same as find
print(x.index("dip"))
# For Isalnum check means wheter it is A-Z, a-z, 0-9
no = "12amihelloHW"
print(no.isalnum())
# For Isalpha check means wheter it is A-Z, a-z
no = "amihelloHW"
print(no.isalpha())
# For Islower check means wheter it is a-z
no = "amihello"
print(no.islower())
# For Isupper check means wheter it is A-Z
no1 = "AMIHELLO"
print(no.isupper())
# For Isprintable check means wheter it is printable or NOT(\n)
no = "amihello"
print(no.isprintable())
# For Isspace check ->
spa = "        "
print(spa.isspace())
# For Istitile check (when all the words first letter is Capital->
isss = "I Am a Good Boy"
print(isss.istitle())
# For make Titile ->
osss = "i am a boy"
print(osss.title())
# For Swap Case (swap all the letters) ->
swap1 = "Soumodip"
print(swap1.swapcase())
