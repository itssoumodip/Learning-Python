'''
f = open('myfile.txt', 'r')
i=0
while True:
    i+=1
    line = f.readline()
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"Marks of student {i} in Engllish is : {m1*2}")
    print(f"Marks of student {i} in Hinglish is : {m2*2}")
    print(f"Marks of student {i} in Monglish is : {m3*2}")
    print(line)
'''
f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

