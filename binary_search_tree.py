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
    def __init__(self, node: Node) -> None:
        self.base_node = node
    
    def __balancetree__(self) -> None:
        pass

    def add_node(self, node: Node) -> bool:
        """
        Rebalances the tree afterwards.

        Nodes are not allowed to have the same key of an existing node. This will result in an
        unsuccessful add_node call.
        """
        if not isinstance(node, Node):
            return False

        current_node = self.base_node

        while True:
            # Loop until node is inserted or invalid
            if node.key == current_node.key:
                return False
            if node.key > current_node.key and not current_node.right:
                print(current_node.key, node.key)
                current_node.right = node
                break
            if node.key < current_node.key and not current_node.left:
                print(current_node.key, node.key)
                current_node.left == node
                break

            current_node = current_node.right if node.key > current_node.key else current_node.left            

        return True
    
    def remove_node(self, key: int) -> bool:
        """
        Rebalances the tree afterwards.
        """
        return True

    def get_value(self, key: int) -> any:
        
        current_node = self.base_node
        print("get value")
        while True:
            # Loop intil node is found or bottom of tree reached
            if not current_node:
                break
            if key == current_node.key:
                return current_node.value
            print(current_node.key)
            current_node = current_node.right if key > current_node.key else current_node.left

        return None    
