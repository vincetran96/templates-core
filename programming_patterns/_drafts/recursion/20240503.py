"""2024-05-03"""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.tail = None


class LinkedList:
    def __init__(self) -> None:
        self.root = None

    def append(self, data):
        node = Node(data=data)
        if not self.root:
            self.root = node
        else:
            end = self.root
            while end.tail:
                end = end.tail
            end.tail = node

    def show(self):
        print("showing")
        node = self.root
        while node:
            print(node.data)
            node = node.tail

    def reverse(self):
        res = LinkedList()
        node = self.root
        while node:
            new_node = Node(node.data)
            if res.root:
                new_node.tail = res.root
                res.root = new_node
            else:
                res.root = new_node
            node = node.tail
        return res


l = LinkedList()
print(l.root)
l.append(1)
l.show()
l.append(2)
l.show()
l.append(3)
l.show()
n = l.reverse()
n.show()
l.append(4)
n.show()
l.show()
m = n.reverse().reverse()
m.show()
