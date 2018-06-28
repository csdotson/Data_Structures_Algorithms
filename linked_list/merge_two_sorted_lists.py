'''
Problem: Given two sorted linked lists, merge them so entries in merged list are in ascending order
'''
import list_node as node

def merge_two_sorted_lists(L1, L2):
    temp_head = temp_tail = node.ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            temp_tail.next = L1
            L1 = L1.next
        else:
            temp_tail.next = L2
            L2 = L2.next
        temp_tail = temp_tail.next
    
    temp_tail.next = L1 or L2
    return temp_head.next


if __name__ == "__main__":
    L1 = node.ListNode(2)
    node2 = node.ListNode(3)
    node3 = node.ListNode(5)
    node4 = node.ListNode(7)

    L1.next = node2
    node2.next = node3
    node3.next = node4

    L2 = node.ListNode(1)
    node_2 = node.ListNode(4)
    node_3 = node.ListNode(6)

    L2.next = node_2
    node_2.next = node_3
