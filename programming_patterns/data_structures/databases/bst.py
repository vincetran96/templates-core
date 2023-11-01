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

    def num_children(self) -> int:
        """Returns the number of [direct] children
        """
        return sum((self.left != None, self.right != None))

    def lr(self, value: int) -> 'Node':
        """Returns the left or right node
        depending on the value vs this node's value
        """
        if value < self.value:
            return self.left
        return self.right

    def is_parent(self, node: 'Node') -> bool:
        """Returns if this node is parent of the provided node
        """
        return node is self.left or node is self.right

    def set_left(self, node: 'Node') -> None:
        """Explicitly sets left node
        """
        self.left = node

    def set_right(self, node: 'Node') -> None:
        """Explicitly sets right node
        """
        self.right = node

    def set_child(self, node: 'Node') -> None:
        """Sets a child node depending on the
        value of the node vs this node's value
        """
        if node.value < self.value:
            self.left = node
        elif node.value > self.value:
            self.right = node
        else:
            raise ValueError(
                f"The child candidate has the same value as the parent: {self.value}"
            )
        node.parent = self

    def set_parent(self, node: 'Node') -> None:
        """Sets a parent for this node
        """
        if node.parent is self:
            raise AttributeError("Cannot set a child node to be parent")
        self.parent = node

    def remove_child(self, node: 'Node') -> None:
        """Removes a child node from this node
        """
        if not (node is self.left or node is self.right):
            raise AttributeError("Node is not a child of self")
        if node is None:
            raise TypeError("Node must not be None")
        if node.value < self.value:
            self.left = None
        else:
            self.right = None


class Tree:
    """Rough implementation of Binary Search Tree
    """
    def __init__(self, root_value: int):
        self.root = Node(root_value)
        self.traverse_modes = ('in-order', 'pre-order', 'post-order')

    def _locate_value(self, value: int) -> Tuple[Node, Node]:
        """Travels downward from root to a node having this value

        Returns:
            - The node having this value
            - The node's parent node

        Args:
            value: (int)
        """
        def _trav(node: Node, prev_node: Node):
            if node is None or value == node.value:
                return node, prev_node
            return _trav(node.lr(value), node)

        return _trav(self.root, self.root)

    def traverse(self, mode: str) -> str:
        """Traversal in string

        Returns:
            A string representing order of traversal

        Args:
            mode: (str) - String presenting mode
        """
        if mode not in self.traverse_modes:
            raise ValueError("Must specify mode")

        def _trav(node: Node):
            if node is None:
                return ""

            traverse_mode_map = {
                'in-order':
                    _trav(node.left) + f" {{{str(node.value)}}} " + _trav(node.right),
                'pre-order':
                    f" {{{str(node.value)}}} " + _trav(node.left) + _trav(node.right),
                'post-order':
                    _trav(node.left) + _trav(node.right) + f" {{{str(node.value)}}} "
            }
            return traverse_mode_map[mode]

        return "[" + _trav(self.root).strip() + "]"

    def search(self, value: int) -> int:
        """Searches for a value in the tree

        Returns:
            1 if found, 0 if not

        Args:
            value: (int)
        """
        node, _ = self._locate_value(value)
        if node:
            return 1
        return 0

    def insert_value(self, value: int) -> None:
        """Adds a value to the tree

        Args:
            value: (int)
        """
        node, parent = self._locate_value(value)
        if node is None:
            new_node = Node(value)
            parent.set_child(new_node)
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

        If the value is not found in the tree, raise Exception

        If the node containing the value has no children,
        remove the node from the tree depending on where
        the node is respective to its parent (left or right)

        If the node containing the value has children:

        - If the node has only 1 child, replace the node
          with the node's child (i.e., promote the
          node's child to be the child of the node's parent)
        - If the node has children on both sides, find the
          successor by looking for the leftmost node from the
          right child of the node, then replace the node with
          the successor (i.e., promote the successor to be the
          child of the node's parent)

        But we must take care of the case where the successor
        has child on the right?

        - The successor must only have 1 child on the right,
          because the successor is the leftmost node already

        Args:
            value: (int)
        """
        def _find_successor(node: Node, prev_node: Node):
            """Finds the leftmost node on the
            right branch of this node
            """
            if node.left is None:
                return node, prev_node
            return _find_successor(node.left, node)

        node, node_parent = self._locate_value(value)
        if node is None:
            raise ValueError(f"Value does not exist in tree: {value}")
        if node is self.root and len(self) == 1:
            raise RuntimeError("Cannot delete the root node from a single-node tree")
        match node.num_children():
            case 0:
                node_parent.remove_child(node)
            case 1:
                node_parent.set_child(node.left or node.right)
            case _:
                succ, succ_parent = _find_successor(node.right, node)
                if node.is_parent(succ):
                    node_parent.set_child(succ)
                    succ.set_child(node.left)
                else:
                    succ_parent.set_child(succ.right)
                    succ.set_child(node.left)
                    succ.set_child(node.right)

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

    def __len__(self) -> int:
        """Count of all nodes in the tree
        """
        def _count(node: Node):
            if node is None:
                return 0
            return 1 + _count(node.left) + _count(node.right)

        return _count(self.root)


if __name__ == "__main__":
    node0 = Node(10)
    node1 = Node(11)
    node2 = Node(12)
    node0.set_child(node1)
    print(f"node0 num children: {node0.num_children()}")
    print(f"node1: {node0.right.value}")
    print(f"node0: {node1.parent.value}")
    node0.remove_child(node1)
    node0.set_child(node2 or None)
    print(f"node2: {node0.right.value}")
    print(f"Is node2 child of node0: {node0.is_parent(node2)}")

    tree = Tree(27)
    tree.insert_value(14)
    tree.insert_values([35, 12, 20, 10, 13, 17, 22, 9, 16, 18, 23])
    print(tree)
    print("Traverse:")
    print(tree.traverse("in-order"))
    print(tree.traverse("pre-order"))
    print(tree.traverse("post-order"))
    print(f"Length of tree: {len(tree)}")
    print("Sum all values:")
    print(tree.sum_values())
    print(len(tree))
    print("Delete:")
    tree.delete(20)
    print(tree)
    print(tree.traverse("in-order"))
    print(f"Length of tree: {len(tree)}")

    print("Delete from single-node tree")
    tree1 = Tree(100)
    print(tree1)
    try:
        tree1.delete(100)
    except RuntimeError as exc:
        print(f"Exception: {exc}")
    print(tree1)

    tree2 = Tree(2)
    tree2.insert_values([1, 3])
    print(tree2)
    tree2.delete(2)
    print(tree2)
