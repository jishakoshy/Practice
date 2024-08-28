class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
class BinarysearchTree:
    def insert(node,key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = insert(node.left,key)
        elif key > node.key:
            node.right = insert(node.right, key)
        return node
    
    def deletenode(self,root,key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.deletenode(root.left,key)
        elif key > root.key:
            root.right = self.deletenode(root.right,key)
        else:
            

__name__ == "__main__":
    tree = BinarysearchTree()
    tree.root = tree.insert(tree.root, 50)
    tree.insert(tree.root, 30)
    tree.insert(tree.root, 20)   