from node import Node


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, node):

        if not self.head:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node


    def add_child(self, parent, child):

        if parent.sub_list is None:
            parent.sub_list = DoubleLinkedList()

        parent.sub_list.append(child)


    def print_multilist(self, level=0):

        if not self.head:
            print("Empty list")
            return

        current = self.head

        while current:

            print("   " * level + f"{current.id} - {current.name}")

            if current.sub_list:
                current.sub_list.print_multilist(level + 1)

            current = current.next