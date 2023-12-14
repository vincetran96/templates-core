"""Linked list containing integers
"""


class Node:
    """Container for data
    """
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node = None  # type: ignore


class SinglyLinkedList:
    """Implementation of Singly Linked List
    """
    def __init__(self) -> None:
        self.head: Node = None  # type: ignore
        self.tail: Node = None  # type: ignore

    def is_empty(self) -> bool:
        """Checks empty"""
        return self.head is None

    def add(self, value: int) -> None:
        """Adds Node at end
        """
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def get_head(self) -> int:
        """Gets head"""
        return self.head.value

    def get_tail(self) -> int:
        """Gets tail"""
        return self.tail.value

    def sort(self):
        """Sorts itself using selection sort"""
        def _sort(base_node: Node, compare_node: Node):
            """Sort helper"""
            if base_node.next is not None:
                if compare_node.value < base_node.value:
                    temp_value = compare_node.value
                    compare_node.value = base_node.value
                    base_node.value = temp_value
                if compare_node.next is not None:
                    _sort(base_node, compare_node.next)
                else:
                    _sort(base_node.next, base_node.next.next)

        if len(self) > 1:
            _sort(self.head, self.head.next)

    def __repr__(self) -> str:
        def _disp(node: Node, final_str: str = "") -> str:
            if node is None:
                return final_str
            return _disp(node.next, final_str + ", " + str(node.value))

        return "[" + _disp(self.head).strip(", ") + "]"

    def __len__(self) -> int:
        def _getsize(node: Node, acc: int):
            if node is None:
                return acc
            return _getsize(node.next, acc + 1)

        return _getsize(self.head, 0)


if __name__ == "__main__":
    n0 = Node(10)
    print(n0.next)

    sl = SinglyLinkedList()
    print(sl.is_empty())
    sl.add(50)
    print(f">> sl head={sl.get_head()}, sl tail={sl.get_tail()}")
    sl.add(2)
    print(f">> sl head={sl.get_head()}, sl tail={sl.get_tail()}")
    print(f"sl head.next={sl.head.next.value}")
    print("sl as string:")
    print(sl)
    sl.add(65)
    sl.add(12)
    print(f">> sl head={sl.get_head()}, sl tail={sl.get_tail()}")
    print(f"sl head.next={sl.head.next.value}")
    print("sl as string:")
    print(sl)
    print(len(sl))
    sl.sort()
    print(sl)
