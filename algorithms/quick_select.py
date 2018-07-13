'''
Python implementation of quickselect (RSelect) algorithm
A: Original array
left, right: left-most and right-most indices of array
i: order of the statistic to return
'''
import random

def quick_select(A, left, right, i):
    if right - left <= 1:
        return A[left]

    pivot_location = partition(A, left, right)
    if pivot_location == i:
        return A[pivot_location]
    if pivot_location > i:
        return quick_select(A, left, pivot_location, i)
    if pivot_location < i:
        return quick_select(A, pivot_location+1, right, i - pivot_location)

def partition(A, left, right):
    rand_index = random.randint(left, right-1)
    pivot = A[rand_index]
    swap(A, left, rand_index)

    i = left + 1
    for j in range(i, right):
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
    
    swap(A, left, i-1)
    return i-1


def swap(A, first, second):
    A[first], A[second] = A[second], A[first]
