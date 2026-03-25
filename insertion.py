class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def insert_at_position(self, data, pos):
        node = Node(data)

        if pos == 1:
            node.next = self.head
            self.head = node
            return

        temp = self.head
        for _ in range(pos - 2):
            temp = temp.next

        node.next = temp.next
        temp.next = node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

sll = SinglyLinkedList()

n = int(input("Enter number of nodes to insert at end: "))
for i in range(n):
    data = int(input(f"Enter data for node {i+1}: "))
    sll.insert_at_end(data)

data = int(input("Enter data to insert at beginning: "))
sll.insert_at_beginning(data)

data = int(input("Enter data to insert at a position: "))
pos = int(input("Enter position: "))
sll.insert_at_position(data, pos)

print("\nSingly Linked List:")
sll.display()
