f = open("demo.txt", "rt") #read and text mode (default)

file = f.read() #reads entire file
print(file)
line1 = f.readline() #reads one line
print(line1)
lines = f.readlines() #reads all lines into a list
print(lines)

f.close()

with open("demo.txt", "rt") as f: #using with statement
    file = f.read()
    print(file)
    line1 = f.readline()
    print(line1)
    lines = f.readlines()
    print(lines)