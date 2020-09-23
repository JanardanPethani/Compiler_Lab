nonTerm = input("Enter Non-terminals: ").split(" ")
Term = input("Enter Terminals: ").split(" ")
productions = {}
for i in nonTerm:
    print(f"Rule for {i}",end=':')
    rule = input().split('/')
    productions[i] = rule
print(productions)
first = {}

def find_term(rule):
    if rule[0] in Term:
        return rule[0]
    if rule[0] in nonTerm:
        returnLst = []
        prodRules_i = productions[rule[0]]
        for rule_1 in prodRules_i:
            if rule_1[0] in Term:
                returnLst.append(rule_1[0])
            elif rule_1[0] in nonTerm:
                temp_Lst = find_term(rule_1[0])
                returnLst.extend(temp_Lst)
            elif rule_1 == 'eps':
                if len(rule) > 1:
                    temp_Lst = find_term(rule[1])
                    returnLst.extend(temp_Lst)
                returnLst.append('eps')
        return returnLst

def f_first(nonTerm,Term,productions):
    for nT in nonTerm:
        rules = productions[nT]
        for rule in rules:
            # print(nT,'->',rule,end=' first: ')
            if rule == 'eps':
                lst = first.get(nT, [])
                lst.append('eps')
                first[nT] = lst
            elif rule[0] in Term:
                lst = first.get(nT,[])
                lst.append(rule[0])
                first[nT] = lst
            else:
                lst = first.get(nT, [])
                lst_1 = find_term(rule)
                lst_2 = list(dict.fromkeys(lst_1))
                lst.extend(lst_2)
                first[nT] = lst
            print(first)
            
f_first(nonTerm,Term,productions)
print(first)


