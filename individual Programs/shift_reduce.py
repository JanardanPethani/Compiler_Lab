#note sample grammar P->CC/cC,C->d   string :- cd dd or similar to this
#E->E*E/E+E/i     string :- i+i*i or i*i*i+i



if __name__ == "__main__":
    gram=input('enter your production :')
    productions=gram.split(',')
    #print(productions)

    terminal=[]
    non_terminal=[]
    start_symbol=productions[0].split('->')[0]
    #print(start_symbol)
    for i in productions:
        pro=i.split('->')
        if pro[0] not in non_terminal:
            non_terminal.append(pro[0])     # find non terminals
    print("list of non terminal",non_terminal)
    for i in productions:
        pro=i.split('->')
        right_pro=pro[1].split('/')

        for j in right_pro:
            if j=="#":
                continue

            for k in range(0,len(j)):

                if j[k] not in non_terminal :
                    terminal.append(j[k])   #find terminals
    #print("list of terminal",terminal)
    production=[]
    #print(productions)
    for i in productions:
        pro=i.split("->")
        r_pro=pro[1].split("/")
        for j in r_pro:
            t=pro[0]+"->"+j
            production.append(t)

    s=input("enter string which you want to parse :")
    #print(s)
    s=s+"$"
    stack='$'
    for i in s:
        stack=stack+i
        print(stack)
        #print("new start")
        index=-1
        for i in range(len(stack)-1):
            t=stack[index:]
            #print(t)
            index=index-1
            for j in production:
                r_pro=j.split("->")
                if t==r_pro[1]:
                    temp=r_pro[0]
                    stack=stack.replace(t,str(temp))
                    #print("updated stack",stack)
    if stack=="$"+start_symbol+"$":
        print('stack ',stack)
        print("string is part of grammer")
    else:
        print("string is not part of grammer")
        print('stack ',stack)
