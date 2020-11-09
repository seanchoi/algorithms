def noEachOther(string):
    item_num = []
    string_list = []
    string_list[:0] = string    
    print(string_list)
    string_set = sorted(list(set(string)))
    print(string_set)    
    
    for i in range(len(string_set)):
        item_num.append(string.count(string_set[i]))
    print(item_num)

    for s in range(0, len(item_num)-1):
        if item_num[s+1]-item_num[s] > 1 or item_num[s+1]-item_num[s]==0:
            return None
        else:
            new_list = []
            for k in range(item_num[-1]):
                new_list.append(string_set[-1])
                if k > 0:                
                    new_list.append(string_set[-2])
                
            return print(new_list)

    return print(item_num)

noEachOther('aabbccc')