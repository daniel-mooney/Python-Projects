class Node:
    """
    The class node is used as an element of a data structure class, such as in BinaryTree in this
    specific example. The class attributes are taylored to the data structure it is to be used in.
    """   
    def __init__(self, key: int, value: any) -> None:
        self.key = key
        self.value = value

        # Next Node Pointers - left is less than, right is greater than.
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, node: Node) -> None:
        self.base = node
    
    def __balancetree__(self) -> None:
        pass

    def add_node(self, node: Node) -> bool:
        """
        Rebalances the tree afterwards.

        Nodes are not allowed to have the same key of an existing node. This will result in an
        unsuccessful add_node call.
        """


        return True
    
    def remove_node(self, key: int) -> bool:
        """
        Rebalances the tree afterwards.
        """
        return True

    def get_value(self, key: int) -> any:
        pass