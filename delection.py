class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def insert(data):
    global head
    new = Node(data)

    if head is None:
        head = new
        return

    temp = head
    while temp.next:
        temp = temp.next

    temp.next = new

def delete(key):
    global head

    temp = head
    prev = None

    if temp and temp.data == key:
        head = temp.next
        return

    while temp and temp.data != key:
        prev = temp
        temp = temp.next

    if temp is None:
        print("Node not found")
        return

    prev.next = temp.next

def display():
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

n = int(input("Enter number of nodes: "))

for i in range(n):
    insert(int(input("Enter value: ")))

print("Linked List:")
display()

delete(int(input("Enter value to delete: ")))

print("After deletion:")
display()

