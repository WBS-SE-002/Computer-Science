class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_left(self, current_node, new_value):
        new_node = TreeNode(new_value)
        if current_node.left is None:
            current_node.left = new_node
        else:
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, new_value):
        new_node = TreeNode(new_value)
        if current_node.right is None:
            current_node.right = new_node
        else:
            new_node.right = current_node.right
            current_node.right = new_node


bt = BinaryTree('R')

bt.insert_left(bt.root, 'A')   # nodeA
bt.insert_right(bt.root, 'B')  # nodeB

nodeA = bt.root.left
nodeB = bt.root.right

bt.insert_left(nodeA, 'C')
bt.insert_right(nodeA, 'D')

bt.insert_left(nodeB, 'E')
bt.insert_right(nodeB, 'F')

nodeF = nodeB.right
bt.insert_left(nodeF, 'G')

print("root.right.left.value:", bt.root.right.left.value)  # Should print 'E'

# -- Now build the tree --

#      R
#     / \
#    A   B
#   / \ / \
#  C  D E  F
#        /
#
