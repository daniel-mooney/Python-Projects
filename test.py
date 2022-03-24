from binary_search_tree import *

tree = BinaryTree(Node(10, 24))

tree.add_node(Node(5, "cool"))
tree.add_node(Node(12, 4.23))
x = tree.add_node(Node(11, 65))
tree.add_node(Node(14, 4.29))
tree.add_node(Node(13, 7.9))
tree.add_node(Node(6, "ahhhh"))
tree.add_node(Node(8, "test"))

print(tree.get_value(5))
# print(x)
