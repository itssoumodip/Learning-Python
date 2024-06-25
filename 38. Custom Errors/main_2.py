## Raising Custom errors
# In python, we can raise custom errors by using the `raise` keyword.

x = int(input("Enter a No. between 5 and 9 : "))
if (x<5 or x>9):
    raise ValueError("Invalid value entered")   ##raise value Error