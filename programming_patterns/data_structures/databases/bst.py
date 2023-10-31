"""Binary search tree containing integers
"""
from typing import Tuple, List


class Node:
    """Container for data
    """
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None

    def has_children(self) -> bool:
        """Checks if the node has children
        """
        return self.left is not None or self.right is not None

    def lappend(self, node: Node) -> None:
        """Left append
        """
        self.left = node

    def rappend(self, node: Node) -> None:
        """Right append
        """
        self.right = node


class Tree:
    """Rough implementation of Binary Search Tree
    """
    def __init__(self, root_value: int = None):
        root: Node = None
        if root_value:
            root = Node(root_value)
        self.root = root

    def _traverse(
        self, value: int, node: Node,
        prev_node: Node = None, is_left: bool = True
    ) -> Tuple[Node, Node, bool]:
        """Traverses to a node having value

        Returns (as a tuple):
        - The node
        - Previous node
        - Whether the current travel is left or right
        """
        if node is None or value == node.value:
            return node, prev_node, is_left
        if value > node.value:
            return self._traverse(value, node.right, node, False)
        return self._traverse(value, node.left, node, True)

    def _change_child(self, node: Node, child_node: Node, is_left: bool):
        """Changes this node's child node
        into another Node instance
        """
        if is_left:
            node.left = child_node
        else:
            node.right = child_node

    def search(self, value: int) -> Node:
        """Searches for a value in the tree
        """
        node, _, _ = self._traverse(value, self.root)
        if node:
            return 1
        return 0

    def add_value(self, value: int) -> None:
        """Adds a value to the tree
        """
        node, prev_node, is_left = self._traverse(value, self.root)
        if node is None:
            self._change_child(prev_node, Node(value), is_left)
        else:
            raise ValueError(f"Value already exists in tree: {value}")

    def add_values(self, values: List[int]) -> None:
        """Adds multiple values to the tree

        Adds using the order of the values provided
        """
        for value in values:
            self.add_value(value)

    def delete(self, value: int) -> None:
        """Deletes a value from the tree

        Define an auxiliary function `find_successor`

        The idea is as follows:
        - If the value is not found in the tree, raise Exception
        - If the node containing the value has no children,
          remove the node from the tree depending on where
          the node is respective to its parent (left or right)
        - If the node containing the value has children
            - If the node has only 1 child on the left, replace
            the node with the node's child (i.e., promote the
            node's child to be the child of the node's parent)
            - If the node has children on both sides, find the
            successor by looking for the leftmost node from the
            right child of the node, then replace the node with
            the successor (i.e., promote the successor to be the
            child of the node's parent)
        """
        def _find_successor(node: Node, prev_node: Node):
            """Finds the leftmost node on the
            right branch of this node
            """
            if node.left is None:
                return node, prev_node
            return _find_successor(node.left, node)

        node, prev_node, is_left = self._traverse(value, self.root)
        if node is None:
            raise ValueError(f"Value does not exist in tree: {value}")
        if not node.has_children():
            if node is self.root:
                self.root = None
            else:
                self._change_child(prev_node, None, is_left)
        else:
            if node.right is None:
                self._change_child(prev_node, node.left, is_left)
            else:
                succ, succ_prev = _find_successor(node.right, node)
                print(f"Found successor = {succ.value}")
                self._change_child(prev_node, succ, is_left)
                self._change_child(succ, node.left, True)
                self._change_child(succ, node.right, False)
                self._change_child(succ_prev, None, True)

    def sum_values(self) -> int:
        """Calculates sum of all Nodes' values in the tree
        """
        def _sum(node: Node) -> int:
            """Sum helper
            """
            if node is None:
                return 0
            return node.value + _sum(node.left) + _sum(node.right)

        return _sum(self.root)

    def __repr__(self) -> str:
        """String representation, very ugly
        """
        def _show_val(node: Node) -> str:
            if node is None:
                return "None"
            return str(node.value)

        def _disp(node: Node, level: int = 0) -> str:
            if node is None:
                return f"Level {level}: {{{ _show_val(node) }}}"
            return f"Level {level}: {{{_show_val(node)}}}: " \
                f"[ {{{_show_val(node.left)}}}, {{{_show_val(node.right)}}} ]" \
                f"\n{_disp(node.left, level + 1)}" \
                f"\n{_disp(node.right, level + 1)}"

        return _disp(self.root)


if __name__ == "__main__":
    tree = Tree(27)
    print(f"Search for value=2: {tree.search(2)}")
    tree.add_value(14)
    print(f"Search for value=2: {tree.search(2)}")
    tree.add_values([35, 12, 20, 10, 13, 17, 22, 9, 16, 18, 23])
    print(tree)
    print(tree.sum_values())
    print("Deleting")
    tree.delete(20)
    print(tree)

    print("Delete from single-node tree")
    tree1 = Tree(100)
    print(tree1)
    tree1.delete(100)
    print(tree1)
