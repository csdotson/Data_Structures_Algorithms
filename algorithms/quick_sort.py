'''
Python implementation of quicksort algorithm
'''
comparison_count = 0

def quick_sort(A, left, right):
    global comparison_count
    
    if right - left <= 1:
        return 
    
    comparison_count += (right - left - 1)

    pivot_location = partition(A, left, right)
    quick_sort(A, left, pivot_location)
    quick_sort(A, pivot_location+1, right)


def partition(A, left, right):
    # # Choosing first element as pivot:
    # pivot = A[left]

    # # Choosing last element as pivot:
    # pivot = A[right - 1]
    # swap(A, left, right - 1)
    
    # Using median of 3 as pivot
    pivot = median_of_three(A, left, right)

    i = left + 1
    for j in range(i, right):
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
    
    swap(A, left, i-1)
    return i-1


def median_of_three(A, left, right):
    first, last, middle = A[left], A[right - 1], A[(left + right -1)//2]
    values = [first, middle, last]

    for i in range(len(values)):
        for j in range(i+1, len(values)):
            if values[i] > values[j]:
                swap(values, i, j)

    if values[1] == last:
        swap(A, left, right - 1)
    if values[1] == middle:
        swap(A, left, (left + right -1)//2)
    
    return values[1]


def swap(A, first, second):
    A[first], A[second] = A[second], A[first]


# Manipulating content file
with open("int_list.txt") as f: 
    content = f.readlines()

content = [x.strip() for x in content]
content = [int(x) for x in content]