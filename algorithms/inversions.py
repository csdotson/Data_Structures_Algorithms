'''
Python implementation of inversion counting algorithm
'''
inversion_count = 0

def sort_and_count(A):
    if len(A) <= 1:
        return A
    
    mid = len(A)//2
    return merge_and_count_split_inv(sort_and_count(A[:mid]), sort_and_count(A[mid:]))

def merge_and_count_split_inv(B, C):
    global inversion_count
    i, j = 0, 0
    Output = []

    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            Output.append(B[i])
            i += 1
        else: # C[j] < B[i]
            Output.append(C[j])
            j += 1
            inversion_count += (len(B) - i) 

    Output += B[i:]
    Output += C[j:]

    return Output
    
