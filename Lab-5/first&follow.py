n = int(input("Enter number of productions"))
productions = {}
newProductions = {}
for i in range(n):
    prod = input().split('->')
    productions[prod[0]] = prod[1].split('/')
# print(productions)

def find_First(productions):
    first = {}
    for key in productions:
        for rule in productions[key]:
            if rule == 'epsilon':
                lst = first.get(key, list())
                lst.append(rule)
                first[key] = lst
            if rule != 'epsilon' and ( rule[0].islower() or rule[0].isalnum() == False ):
                lst = first.get(key, list())
                lst.append(rule[0])
                first[key] = lst

    def findTermi(rule,firstDict):
        term = []
        # print(firstDict)
        if rule in firstDict:
            term = firstDict[rule]
        else:
            term = findTermi(productions[rule][0][0],firstDict)
        return term

    for key in productions:
        for rule in productions[key]:
            if rule[0].isupper():
                # print(key,rule)
                lst = findTermi(rule[0],first)
                lst1 = first.get(key,[]) + lst
                if 'epsilon' in lst1:
                    lst1.remove('epsilon')
                    if rule[1].islower() or rule[1].isalnum() == False:
                        lst1.extend([rule[1]])
                    else:
                        lst1.extend(findTermi(rule[1],first))
                first[key] = lst1

    return first
print(find_First(productions))

def find_follow(productions):
    