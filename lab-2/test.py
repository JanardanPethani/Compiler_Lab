file = open("Input.txt",'r')
productions = []
for line in file:
    d_line = line.replace(" ","")
    productions.append(d_line)
print(productions)
