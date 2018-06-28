def traverse(L):
    """ Traverse list of nodes, print values """
    while L:
        print(L.data) 
        L = L.next


def search_list(L, key):
    """ Search list for value, return value if present """
    while L and L.data != key:
        L = L.next
    # If key not found in list, L will be null
    return L
