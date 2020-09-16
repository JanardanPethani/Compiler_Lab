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
        rules = productions[rule[0]]
        to_return = []
        for rule in rules:
            if rule[0] in nonTerm:
                to_return.extend(find_term(rule[0]))
            elif rule[0] in Term:
                to_return.append((rule[0]))
        return to_return

def f_follow(nonTerm,Term,productions):
    for nT in nonTerm:
        rules = productions[nT]
        for rule in rules:
            # print(nT,'->',rule)
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
                lst1 = find_term(rule)
                lst.extend(lst1)
                first[nT] = lst

            
f_follow(nonTerm,Term,productions)
print(first)


