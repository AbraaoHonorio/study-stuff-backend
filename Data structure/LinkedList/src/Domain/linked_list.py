import sys

sys.path.append('src')
this = sys.modules[__name__]

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        list = self.head
        while list is not None:
            print(list.value)
            list = list.next
