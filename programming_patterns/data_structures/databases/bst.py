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

    def lappend(self, node: 'Node') -> None:
        """Left append
        """
        self.left = node

    def rappend(self, node: 'Node') -> None:
        """Right append
        """
        self.right = node

    def set_parent(self, node: 'Node') -> None:
        """Sets parent
        """
        self.parent = node


class Tree:
    """Rough implementation of Binary Search Tree
    """
    def __init__(self, root_value: int = None):
        if not root_value:
            raise ValueError("Must provide value for root")
        self.root = Node(root_value)
        self.traverse_modes = ('in-order', 'pre-order', 'post-order')

    def _traverse(self, value: int, node: Node):
        """Traverses downward from this node
        to a node having value

        Returns:
        """
        def _trav(n: Node, prev_n: Node, is_left: bool):
            if n is None or value == n.value:
                return n, prev_n, is_left
            if value > n.value:
                return _trav(n.right, n, False)
            return _trav(n.left, n, True)

        return _trav(node, node, True)

    def traverse(self, mode: str) -> str:
        """Traversal

        Returns: a string representing order of traverssal
        """
        if mode not in self.traverse_modes:
            raise ValueError("Must specify mode")

        def _trav(node: Node):
            if node is None:
                return ""

            traverse_mode_map = {
                'in-order': _trav(node.left) + f" {{{str(node.value)}}} " + _trav(node.right),
                'pre-order': f" {{{str(node.value)}}} " + _trav(node.left) + _trav(node.right),
                'post-order': _trav(node.left) + _trav(node.right) + f" {{{str(node.value)}}} "
            }
            return traverse_mode_map[mode]

        return "[" + _trav(self.root).strip() + "]"

    def search(self, value: int) -> int:
        """Searches for a value in the tree

        Returns:
            - 1 if found, 0 if not
        """
        node, _, _ = self._traverse(value, self.root)
        if node:
            return 1
        return 0

    def insert_value(self, value: int) -> None:
        """Adds a value to the tree
        """
        node, parent, is_left = self._traverse(value, self.root)
        if node is None:
            new_node = Node(value)
            if parent is None:
                self.root = new_node
            else:
                new_node.set_parent(parent)
                if is_left:
                    parent.lappend(new_node)
                else:
                    parent.rappend(new_node)
        else:
            raise ValueError(f"Value already exists in tree: {value}")

    def insert_values(self, values: List[int]) -> None:
        """Adds multiple values to the tree

        Adds using the order of the values provided
        """
        for value in values:
            self.insert_value(value)

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
    tree.insert_value(14)
    tree.insert_values([35, 12, 20, 10, 13, 17, 22, 9, 16, 18, 23])
    print(tree)
    print("Traverse:")
    print(tree.traverse("in-order"))
    print(tree.traverse("pre-order"))
    print(tree.traverse("post-order"))
    print("Sum all values:")
    print(tree.sum_values())
    # tree.insert_value(14)
    # print("Deleting")
    # tree.delete(20)
    # print(tree)

    print("Delete from single-node tree")
    tree1 = Tree(100)
    print(tree1)
    # tree1.delete(100)
    # print(tree1)
