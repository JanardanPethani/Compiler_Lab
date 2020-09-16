n = int(input("Enter number of productions"))
productions= {}
newProductions = {}
for i in range(n):
    prod = input().split('->')
    productions[prod[0]] = prod[1].split('|')

def common_start(sa, sb):
    """ returns the longest common substring from the beginning of sa and sb """
    def _iter():
        for a, b in zip(sa, sb):
            if a == b:
                yield a
            else:
                return
    return ''.join(_iter())

def newRule(lst,alpha):
    newLst = []
    l = len(alpha)
    for string in lst:
        if string == alpha:
            continue
        elif alpha in string[:l+1]:
            newLst.append(string[l:])
        else:
            continue
    newLst.append("∅")
    return newLst

for nonTer,rule in productions.items():
    if len(rule) > 1:
        # get common terminal
        alpha = common_start(rule[0], rule[1])
        # if no common then go to else
        if  alpha != '':
            # first new production
            tempStr = alpha + f"{nonTer}'"
            newProductions[nonTer] = [tempStr]
            for str in rule:
                if alpha not in str:
                    newProductions[nonTer].append(str)
            # second new production
            newProductions[nonTer+"'"] = newRule(rule,alpha)
        else:
            newProductions[nonTer] = rule
    else:
        newProductions[nonTer] = rule
    

print("Given Productions",productions)
print("New Productions",newProductions)
            

            


        



