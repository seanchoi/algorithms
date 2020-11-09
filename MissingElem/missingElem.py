def missingElem(A):
    missingElem = 0
    for i in range(len(A)+1):
        if not i+1 in A:
            missingElem = i+1
        
    return print(missingElem)

missingElem([1])
missingElem([2,3,1,5])