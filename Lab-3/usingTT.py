def takeTT():
    totalSym = list(input("Symbols: ").split())
    totalStates = int(input("How many states: "))
    acceptedState = list(map(int,input("Accepted state numbers :").split()))
    temp = totalStates
    tt = []
    print(f'Enter T.T. values by rows for column {totalSym}')
    while temp > 0:
        tt.append(list(map(int,input().split())))
        temp -= 1
    print(tt)
    return tt, totalSym, acceptedState


def takeAndCheck_Strings(TT,symbols,accStates):
    #take strings to check
    strList = []
    userString = ''
    print("RE: (a+b)*abb")
    while userString != 'null':
        userString = input()
        strList.append(userString)

    #check using TT
        
    for string in strList[:-1]:
        state = 0
        for ch in string:
            prevState = state
            symIndex = symbols.index(ch)
            state = TT[state][symIndex]
            print(prevState,"->",state)

        if state in accStates:
            print(string,"is Accepted")
        else:
            print(string,"is not Accepted")

transTable, Symbols, accState = takeTT()
takeAndCheck_Strings(transTable,Symbols,accState)