def traverse(L):
    """ Traverse list of nodes, print values """
    while L:
        print(L.data) 
        L = L.next


def search_list(L, key):
    """ Search list for value, if present, return List beginning with value """
    while L and L.data != key:
        L = L.next
    # If key not found in list, L will be null
    return L


def insert_after(node, new_node):
    """ Insert new node after node """
    new_node.next = node.next
    node.next = new_node 


def delete_after(node):
    """ Delete node after; assume node is not tail """
    node.next = node.next.next


def size(L):
    """ Number of nodes in linked list """
    count = 0
    while L:
        count += 1
        L = L.next 
    return count


def print_reverse(L):
    nodes = []
    while L:
        nodes.append(L.data)
        L = L.next
    while nodes:
        print(nodes.pop())
