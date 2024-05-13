# BREAK IN LOOP
for i in range(12):
    if (i==10):
        break
    print("10 x", i,"=",i*10)
print("Left the Loop")
print("__________________________________")
# CONTINUE IN LOOP
for i in range (20):
    if(i==10):
        print("OH no!!!")
        continue
    print("10 x", i,"=",i*10)