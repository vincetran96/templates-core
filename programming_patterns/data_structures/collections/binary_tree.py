"""Binary tree containing integers
"""
from typing import Tuple


class Node:
    """Container for data
    """
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None


class Tree:
    """Rough implementation of Binary Tree
    """
    def __init__(self, root_value: int = None):
        root: Node = None
        if root_value:
            root = Node(root_value)
        self.root = root

    def _traverse(
        self, value: int,
        node: Node, prev_node: Node = None, is_left: bool = True
    ) -> Tuple(Node, Node, bool):
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

    def search(self, value: int) -> Node:
        """Searches for a value in the tree
        """
        node, _, _ = self._traverse(value, self.root)
        if node:
            return 1
        return 0

    def add(self, value: int) -> None:
        """Adds a value to the tree
        """
        node, prev_node, is_left = self._traverse(value, self.root)
        if node is None:
            if is_left:
                prev_node.left = Node(value)
            else:
                prev_node.right = Node(value)
        else:
            print(f"Value already exists in tree: {value}")

    def sum_tree(self) -> int:
        """Calculates sum of all elements in the tree
        """
        def _sum(node: Node) -> int:
            """Sum helper
            """
            if node is not None:
                return node.value + _sum(node.left) + _sum(node.right)
            return 0

        return _sum(self.root)

    def __repr__(self) -> str:
        def _show_val(node: Node) -> str:
            if node is None:
                return "None"
            return str(node.value)

        def _disp(node: Node) -> str:
            if node is None:
                return f"{{{ _show_val(node) }}}"
            return f"{{{_show_val(node)}}}: " \
                f"[ {{{_show_val(node.left)}}}, {{{_show_val(node.right)}}} ]" \
                f"\n{_disp(node.left)}" \
                f"\n{_disp(node.right)}"

        return _disp(self.root)


if __name__ == "__main__":
    tree = Tree(5)
    print(f"Search for value=2: {tree.search(2)}")
    tree.add(2)
    print(f"Search for value=2: {tree.search(2)}")
    tree.add(2)
    tree.add(7)
    tree.add(45)
    print(tree)
