def takeIp(file):
    productions = []
    for line in file:
        d_line = line.replace(" ","")
        d_line = d_line.replace("\n","")
        productions.append(d_line)
    return productions

def removeRecursion(productions):
    print(productions)
    for prod in productions:
        if prod.count('|') == 1:
            if prod[0] == prod[3]:
                print("{} is left recursive".format(prod))
                alpha = prod[4]
                bitaIndex = prod.index('|') + 1
                bita = prod[bitaIndex:]
                print("After removing recursion ::")
                print(f"{prod[0]} -> {bita} {prod[0]}'")
                print(f"{prod[0]}' -> {alpha} {prod[0]}' | ∅")
                print("-------------------------------------")
        elif prod.count('|') > 1:
            if prod[0] == prod[3]:
                # print("{} is left recursive".format(prod))
                prod = prod.split('->')
                nonTerminals = prod[1].split('|')
                alpha = f"{prod[0]}' -> "
                bita = f"{prod[0]} -> "
                for i in nonTerminals:
                    if len(i)>=1:
                        if prod[0] == i[0]:
                            alpha += f"{i[1:]}{prod[0]}' | "
                        elif prod[0] not in i:
                            bita += f"{i}{prod[0]}' | "
                print("After removing recursion ::")
                print(bita[:-2])
                print(alpha + 'None')
                print("-------------------------------------")

file = open("Input.txt","r")
prod = takeIp(file)
removeRecursion(prod)
                
                





        
        

