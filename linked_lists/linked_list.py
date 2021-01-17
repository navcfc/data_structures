class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Utility function to print a linked list


def print_linked_list(head):
    print("HEAD", end=' ')
    while head is not None:
        print('->', head.val, end=' ')
        head = head.next
    print('->', " NULL")
