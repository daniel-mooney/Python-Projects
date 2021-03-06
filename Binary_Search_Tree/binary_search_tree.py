

class Node:
    """
    The class node is used as an element of a data structure class, such as in BinaryTree in this
    specific example. The class attributes are taylored to the data structure it is to be used in.
    """   
    def __init__(self, key: int, value: any) -> None:
        self.key = key
        self.value = value

        # Next Node Pointers - left is less than, right is greater than.
        self.left: Node = None
        self.right: Node = None


class BinaryTree:
    def __init__(self, node: Node = None) -> None:
        self.base_node = node
    
    def __balancetree(self) -> None:
        """
        Priority is given to the left node if the left or right nodes in the middle of a deepest path
        both form valid balanced trees.
        """

        # Find deepest path on left and right side of the tree
        left = self.getdeepestpath(self.base_node.left)
        right = self.getdeepestpath(self.base_node.right)
        left.reverse()

        combined_path = left + [self.base_node] + right       
        mid_point = len(combined_path) // 2 if len(combined_path) % 2 == 1 else len(combined_path) // 2 - 1

        self.base_node = combined_path[mid_point]      


    def getdeepestpath(self, node: Node) -> list:

        if not node:
            return []
        
        left = self.getdeepestpath(node.left)
        right = self.getdeepestpath(node.right)

        deepest_path = max(left, right, key = len)

        return [node] + deepest_path

    def __movenodes(self, node: Node, includeParent: bool = False) -> None:
        """
        Used to move the nodes of a removed parent node to somewhere else in the tree.
        """
        if node == None:
            return None

        if includeParent:
            self.add_node(node)
        if node.right:
            self.add_node(node.right)
            self.__movenodes(node.right)
        if node.left:
            self.add_node(node.left)
            self.__movenodes(node.left)
        

    def add_node(self, node: Node) -> bool:
        """
        Rebalances the tree afterwards. If the base node is `None`, then the newly added node will
        become the new base node.

        Nodes are not allowed to have the same key of an existing node. This will result in an
        unsuccessful add_node call.
        """
        if not isinstance(node, Node):
            return False

        if not self.base_node:
            self.base_node = node
            return True

        current_node = self.base_node

        while True:
            # Loop until node is inserted or invalid
            if node.key == current_node.key:
                return False
            if node.key > current_node.key and not current_node.right:
                current_node.right = node
                break
            if node.key < current_node.key and not current_node.left:
                current_node.left = node
                break

            current_node = current_node.right if node.key > current_node.key else current_node.left            

        self.__balancetree()
        return True
    
    def remove_node(self, key: int) -> bool:
        """
        Rebalances the tree afterwards. If the base node is being removed, priority is given
        to the left node of base node as the new base node. If base node has no connected nodes,
        it is set as `None`. 
        """
        if key == self.base_node.key:
            removed_base = self.base_node

            left = self.base_node.left
            right = self.base_node.right
            self.base_node = left if left else right if right else None

            self.__movenodes(removed_base)

        current_node = self.base_node
        removed = False

        while current_node:
            # Loop until node is found or bottom of tree reached
            if current_node.left and current_node.left.key == key:
                self.__movenodes(current_node.left)        # Move removed node's children nodes
                current_node.left = None
                removed = True
                break
            if current_node.right and current_node.right.key == key:
                self.__movenodes(current_node.right)       # Move removed node's children nodes
                current_node.right = None
                removed = True
                break

            current_node = current_node.right if key > current_node.key else current_node.left

        self.__balancetree()
        return removed

    def get_value(self, key: int) -> any:
        """
        Returns `None` if passed key does not exist.
        """
        current_node = self.base_node

        while current_node:
            # Loop intil node is found or bottom of tree reached
            if key == current_node.key:
                return current_node.value

            current_node = current_node.right if key > current_node.key else current_node.left

        return None 


def main():
    tree = BinaryTree()

    tree.add_node(Node(25, "25"))
    tree.add_node(Node(10, "10"))
    tree.add_node(Node(28, "28"))
    tree.add_node(Node(6, "6"))
    tree.add_node(Node(15, "15"))
    tree.add_node(Node(26, "26"))
    tree.add_node(Node(35, "35"))
    tree.add_node(Node(7, "7"))
    tree.add_node(Node(12, "12"))
    tree.add_node(Node(18, "18"))
    tree.add_node(Node(30, "30"))
    tree.add_node(Node(40, "40"))
    tree.add_node(Node(29, "29"))
    tree.add_node(Node(17, "17"))
    tree.add_node(Node(16, "16"))
    tree.add_node(Node(100, "100"))
    tree.add_node(Node(80, "80"))
    tree.add_node(Node(60, "60"))
    tree.add_node(Node(58, "58"))
    tree.add_node(Node(59, "59"))
    tree.add_node(Node(41, "41"))

    print(tree.getdeepestpath(tree.base_node.right))


if __name__ == "__main__":
    main()
