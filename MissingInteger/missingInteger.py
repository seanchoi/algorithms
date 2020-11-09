def missingInt(A):
    A = list(set(A))
    missingElem = 0 
    for i in range(len(A)+1):
        if A[i-1] < 0:
            missingElem = 1
        elif not i+1 in A:
            missingElem = i+1        
    return print(missingElem)

missingInt([1,3,6,4,1,2])    
missingInt([1,2,3])
missingInt([-1, -3])