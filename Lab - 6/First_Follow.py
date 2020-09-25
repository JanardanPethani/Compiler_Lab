# by Dhynesh Parekh
import re

first = []
d_count = []


def first_finder(key):
    for k in re.split("/", production[key]):
        i = 1
        if re.split("||", k)[i] in production:
            temp = first_finder(re.split("||", k)[i])
            i += 1
            while '#' in temp and not not re.split("||", k)[i] and re.split("||", k)[i] in production:
                temp.remove('#')
                temp = first_finder(re.split("||", k)[i])
                i += 1
            if re.split("||", k)[i] not in production and not not re.split("||", k)[i]:
                first.remove('#')
                if re.split("||", k)[i] not in first:
                    first.append(re.split("||", k)[i])
        else:
            if re.split("||", k)[i] not in first:
                first.append(re.split("||", k)[i])
    return first


def follow_finder(key):  ##S->Aa/BCD/e,A->CB/a,B->b/#,C->c/#,D->Ad/d/#
    follow = []
    for i in production:
        if key in production[i]:
            for prod in re.split("/", production[i]):
                if key in prod:
                    j = 1
                    key_index = re.split("||", prod).index(key)
                    prodc = re.split("||", prod)
                    # print("for",key)
                    # print(first)
                    if not not prodc[key_index + j] and prodc[key_index + j] in production:
                        follow = first_finder(prodc[key_index + j])
                        # print(prod,"first of 1",prodc[key_index+j],follow)
                        j += 1
                        while '#' in follow and not not prodc[key_index + j] and prodc[key_index + j] in production:
                            follow.remove('#')
                            follow = first_finder(prodc[key_index + j])
                            # print(prod,"first of 2",prodc[key_index+j],follow)
                            j += 1
                        if not not prodc[key_index + j] and prodc[key_index + j] not in production:
                            follow.remove('#')
                            if prodc[key_index + j] not in follow:
                                follow.append(prodc[key_index + j])
                                # print(prod,"first of 3",prodc[key_index+j],follow)
                        elif '#' in follow and not prodc[key_index + j]:
                            if '#' in follow:
                                follow.remove('#')
                            if key == i:
                                return follow
                            follow.extend(follow_finder(i))
                            follow = list(set(follow))
                            # print(prod,"follow of",i,follow)
                    elif not not prodc[key_index + j] and prodc[key_index + j] not in production:
                        if prodc[key_index + j] not in follow:
                            follow.append(prodc[key_index + j])
                            # print(prod,"first of 4",prodc[key_index+j],follow)
                    else:
                        if key == i:
                            return follow
                        follow.extend(follow_finder(i))
                        follow = list(set(follow))
                        # print(prod,"follow of",i,follow)
    global d_count
    if not follow and (not d_count and key not in d_count) or (not not d_count and key in d_count):
        follow = ['$']
        d_count.append(key)
    return follow


grammer = input("Enter all productions of grammer seperated by comma: ").split(",")
production = {}
dicFirst = {}
dicFollow = {}
for i in grammer:
    production[re.split("->", i)[0]] = re.split("->", i)[1]
print("Given Grammer:\n", production)
for key in production:
    key_first = first_finder(key)
    print("First(", key, "):", key_first)
    dicFirst[key] = list(key_first)
    first.clear()
    key_follow = follow_finder(key)
    print("Follow(", key, "):", key_follow)
    dicFollow[key] = key_follow
    first.clear()
