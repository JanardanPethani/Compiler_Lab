def First(st):
    list = []
    for s in st:
        for index, c in enumerate(s):
            if c in t:
                list.append(c)
                break
            elif c in nt:
                temp = First(p[c])
                if "ϵ" in temp and (index + 1) < len(s):
                    if s[index + 1] in t:
                        temp.append(s[index + 1])
                    elif s[index + 1] in nt:
                        temp.extend(p[s[index + 1]])
                        temp.remove("eps")
                list.extend(temp)
                break
    l = []
    for c in list:
        if c not in l:
            l.append(c)
    return l


def Follow(nont, d):
    tem = []
    for k in d.keys():
        for i, c in enumerate(d[k]):
            if nont == 'S':
                tem.append('$')
            if nont in c:
                index = c.find(nont)
                if len(c) <= index + 1:
                    tem.extend(Follow(k, d))
                else:
                    f=[]
                    while len(c) > index+1:
                        f.extend(First(c[index + 1]))
                        if 'ϵ' in f:
                            f.remove('eps')
                            f.extend(Follow(k, p))
                        index += 1
                    tem.extend(f)
    l = []
    for c in tem:
        if c not in l:
            l.append(c)
    return l


nt = input("Enter non terminals :").split(" ")
t = input("Enter terminals :").split(" ")
t.append("eps")
n = int(input("Enter number of productions terminals :"))
p = {}
for i in range(n):
    temp = [input().split("->")]
    temp[0][1] = temp[0][1].split("|")
    p.update({temp[0][0]: temp[0][1]})
follow = []
for i in nt:
    follow.append([i, Follow(i, p)])
print(follow)
