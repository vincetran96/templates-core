"""Depth-first-search and Breadth-first-search
"""
class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def append(self, data: int):
        """Let's ignore case when data exists"""
        new_node = Node(data=data)
        if not self.root:
            self.root = new_node
        else:
            node = self.root
            while node:
                if data < node.data:
                    if not node.left:
                        node.left = new_node
                        new_node.parent = node
                        break
                    node = node.left
                elif data > node.data:
                    if not node.right:
                        node.right = new_node
                        new_node.parent = node
                        break
                    node = node.right

    def show_depth_first(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def show_breadth_first(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


t = BinaryTree()
t.append(10)
t.append(7)
t.append(9)
t.append(6)
t.append(5)
t.append(8)
t.show_depth_first()
t.show_breadth_first()
