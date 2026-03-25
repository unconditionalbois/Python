class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.right.right = Node(30)

temp = root
while temp.left:
    temp = temp.left

print("Minimum value:", temp.value)

temp = root
while temp.right:
    temp = temp.right

print("Maximum value:", temp.value)
