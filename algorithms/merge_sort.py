'''
Python implementation of merge sort algorithm
'''
def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    mid = len(alist)//2
    return merge(merge_sort(alist[:mid]), merge_sort(alist[mid:]))
    

def merge(L1, L2):
    i, j, Output = 0, 0, []

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            Output.append(L1[i]) 
            i += 1
        else:
            Output.append(L2[j])
            j += 1

    Output += L1[i:]
    Output += L2[j:]

    return Output