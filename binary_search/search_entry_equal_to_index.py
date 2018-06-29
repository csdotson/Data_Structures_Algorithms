'''
Problem 11.2: Search a sorted array (of distinct values) for an entry equal to its index
'''
def search_entry_equal_to_index(A):
    left, right, result = 0, len(A)-1, -1
    while left <= right:
        mid = (left + right) // 2
        difference = A[mid] - mid
        if difference == 0:
            return mid
        elif difference > 0:
            right = mid - 1
        else:
            left = mid + 1
    return -1