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
        node = self.root
        while node:
            print(node.data)
            if node.left:
                node = node.left
            else:
                while node:
                    if (
                        node.parent
                        and node.parent.right
                        and node.parent.right is not node
                    ):
                        node = node.parent.right
                        break
                    node = node.parent


t = BinaryTree()
t.append(10)
t.append(7)
t.append(9)
t.append(6)
t.append(5)
t.append(8)
t.append(12)
t.append(11)
t.show_depth_first()
