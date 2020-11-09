def solution(S, K):
    item_num = []
    string_list = []
    string_list[:0] = S   
    string_list = sorted(list(set(string_list)))
    print(string_list)
    for i in range(len(string_list)):
        item_num.append(S.count(string_list[i]))
    print(item_num)

    new_string = ""
    for j in range(len(item_num)-1):                
            new_string += str(item_num[j]) + str(string_list[j])                  
            
    return print(new_string)
    
solution('ABBBCCDDCCC', 3)