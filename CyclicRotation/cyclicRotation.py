"""
An array A consisting of N integers is given. Rotation of the array means 
that each element is shifted right by one index, and the last element of the array 
is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] 
is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]
"""

def cyclicRotation(a, k = 0):        
    temp_list = []
    if a == []:
        return
    for i in range(k):
        temp_list.append(a[len(a)-1])
        a.pop()
        a = temp_list + a
        temp_list = []
    return print(a)

cyclicRotation([1,2,3,4], 4)
cyclicRotation([0,0,0], 1)
cyclicRotation([3,8,9,7,6], 3)
cyclicRotation([], 0)
