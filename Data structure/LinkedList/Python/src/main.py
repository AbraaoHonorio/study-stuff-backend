from src.Domain.linked_list import LinkedList, Node


def main():
    list = LinkedList()
    list.head = Node("1")
    node1 = Node("2")
    node2 = Node("3")
    list.head.next = node1
    node1.next = node2
    list.listprint()

if __name__ == '__main__':
    main()