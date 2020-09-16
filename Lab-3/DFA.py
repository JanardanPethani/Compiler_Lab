# Re = (a+b)*abb

def state1(char):
    if char == 'a':
        currDfaState = 2
    elif char == 'b':
        currDfaState = 1
    return currDfaState


def state2(char):
    if char == 'a':
        currDfaState = 2
    elif char == 'b':
        currDfaState = 3
    return currDfaState


def state3(char):
    if char == 'a':
        currDfaState = 2
    elif char == 'b':
        currDfaState = 4
    return currDfaState

def state4(char):
    if char == 'a':
        currDfaState = 2
    elif char == 'b':
        currDfaState = 1
    return currDfaState

def isAccpted(string):
    currDfaState = 1

    for char in string:
        if currDfaState == 1:
            currDfaState = state1(char)
            print("1->",currDfaState)
        elif currDfaState == 2:
            currDfaState = state2(char)
            print("2->",currDfaState)
        elif currDfaState == 3:
            currDfaState = state3(char)
            print("3->",currDfaState)
        elif currDfaState == 4:
            currDfaState = state4(char)
            print("4->",currDfaState)
        else:
            return 0
    if currDfaState == 4:
        return True
    else:
        return False

strList  = []
userString = ''
print("RE: (a+b)*abb")
while userString != 'null':
    userString = input()
    strList.append(userString)

for string in strList[:-1]:
    if isAccpted(string):
        print(string,"Accepted")
    else:
        print(string,"Not Accepted")



