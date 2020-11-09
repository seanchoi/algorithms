"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:
"""
def binaryGap(num):
    binary = bin(num)[2:]
    print(binary)
    gap_count_length = []
    start=0
    length=0
    gap=0    
    for i in range(len(binary)):     
        if binary[i] == "1":
            if start == 0:
                start = 1
            else:
                start += 1
                gap += 1
                gap_count_length.append(length)
                length = 0
        elif binary[i] == "0":
            length += 1     
    max_gap = 0
    if not gap_count_length:
        max_gap = 0
    else:                          
        print(gap_count_length)
        max_gap = gap_count_length[0]             
        for i in range(len(gap_count_length)):        
            if gap_count_length[i] > max_gap:
                max_gap = gap_count_length[i]                
    
    return max_gap

binaryGap(1041)
binaryGap(32)
binaryGap(66561)
            