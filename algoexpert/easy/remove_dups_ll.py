# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    start = linkedList

    while start.next is not None:
        if start.value == start.next.value:
            start.next = start.next.next
        else:
            start = start.next
    return linkedList
