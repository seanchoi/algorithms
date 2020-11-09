def oddOccurence(A):
    sorted_list = list(set(A))
    unpair_item = []
    for i in range(len(sorted_list)):
        item = sorted_list[i]
        check = 0
        for s in range(len(A)):
            if item == A[s]:
                check += 1
        if check%2 == 1:
            unpair_item.append(sorted_list[i])
    return print(unpair_item)

oddOccurence([3,3,5,5,7,7,9])
oddOccurence([3,5,5,5,7,7,9])
