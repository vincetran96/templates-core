'''Linked list containing integers
'''


class Node:
    '''Container for data
    '''
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Node = None # type: ignore


class SinglyLinkedList:
    '''Implementation of Singly Linked List
    '''
    def __init__(self) -> None:
        self.head: Node = None # type: ignore
        self.tail: Node = None # type: ignore 

    def is_empty(self) -> bool:
        return self.head is None

    def add(self, data: int) -> None:
        '''Adds Node at end
        '''
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def get_head(self) -> int:
        return self.head.data

    def get_tail(self) -> int:
        return self.tail.data

    def display_as_str(self) -> str:
        def _disp(node: Node, final_str: str = "") -> str:
            if node is None:
                return final_str
            return _disp(node.next, final_str + ", " + str(node.data))

        return "[" + _disp(self.head).strip(", ") + "]"


if __name__ == "__main__":
    n0 = Node(10)
    print(n0.next)

    sl = SinglyLinkedList()
    print(sl.is_empty())
    sl.add(1)
    print(f">> sl head={sl.get_head()}, sl tail={sl.get_tail()}")
    sl.add(2)
    print(f">> sl head={sl.get_head()}, sl tail={sl.get_tail()}")
    print(f"sl head.next={sl.head.next.data}")
    print(f"sl as string={sl.display_as_str()}")
    sl.add(3)
    print(f">> sl head={sl.get_head()}, sl tail={sl.get_tail()}")
    print(f"sl head.next={sl.head.next.data}")
    print(f"sl as string={sl.display_as_str()}")
