

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None
# inorder, preorder, postorder
    def inorder(self,node,result=None):
        if result is None:
            result = []
        if node:
            self.inorder(node.left,result)
            result.append(node.val)
            self.inorder(node.right,result)

# preorder => root, left, right
    def preorder(self,node,result = None):
        if result is None:
            result = []
        if node:
            result.append(node.value)
            self.preorder(node.left,result)
            self.preorder(node.right,result)
        
# postorder => left, right, root
    def postorder(self,node,result = None):
        if result is None:
            result = []
        if node:
            self.postorder(node.left,result)
            self.postorder(node.right,result)
            result.append(node.value)

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("Inorder traversal:", tree.inorder(tree.root))  # Output: [4, 2, 5, 1, 3]
    print("Preorder traversal:", tree.preorder(tree.root))  # Output: [1, 2, 4, 5, 3]
    print("Postorder traversal:", tree.postorder(tree.root))  # Output: [4, 5, 2, 3, 1]