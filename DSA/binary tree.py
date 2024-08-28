                # using array and linked used for implementation of binary tree
# here using linked list for implementation
    # logic behind of binary_tree is left value less than root and root value is less than right
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binary_tree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):                  
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data,node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data,node.right)

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

tree = binary_tree()
tree.insert(5)
tree.insert(10)
tree.insert(8)
tree.insert(1)
tree.insert(20)
tree.insert(11)
tree.insert(4)

tree.inorder(tree.root)   
       
        