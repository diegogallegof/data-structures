class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        new_node = TreeNode(val)
        
        if self.root is None:
            self.root = new_node
        else:
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                if node.left is None:
                    node.left = new_node
                    break
                elif node.right is None:
                    node.right = new_node
                    break
                else:
                    queue.append(node.left)
                    queue.append(node.right)
    
    def search(self, val):
        if self.root is None:
            return False
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.val == val:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
"""
In this implementation, each node of the binary tree is represented by a 
TreeNode object with a val attribute for the node's value, and left and 
right attributes for its left and right child nodes, respectively.

The BinaryTree class has an insert method to add a new node to the tree. 
It does so by traversing the tree using a queue and inserting the new node 
as a child of the first node it encounters with an empty left or right child.

The search method searches for a node with a given value in the tree by 
traversing the tree using a queue and comparing each node's value to the target value.

Here's an example of how you can use this implementation to create a binary 
tree and search for a value:

"""

# create a binary tree
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

# search for a value
print(tree.search(3)) # True
print(tree.search(6)) # False