class Node:
    def __init__(self, data):
        self.data= data
        self.right = None
        self.left= None

class AVL:
    def  __init__(self):
        self.root= None
    # iterate through the tree to reach the leftmost leaf
    def smallest_element(self, node):
        if node is None:
            return None
        current= node
        while current.left:
            current= current.left
        return current.data
    # or do it recursively like this:
    def recursive_smallest_element(self, node):
        if node is None:
            return None
        if node.left is None:
            return node.data
        return self.smallest_element(node.left)
    
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

avl= AVL()
avl.root= root
# Run the test
print("Smallest element:", avl.smallest_element(avl.root))
print("Smallest element:", avl.recursive_smallest_element(avl.root))
