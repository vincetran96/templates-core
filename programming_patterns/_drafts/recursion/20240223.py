"""2024-02-23"""


def sort0(lst):
    """Merge sort"""
    if len(lst) == 1:
        return lst

    def merge(l1, l2):
        """Merges 2 lists"""
        m = []
        while l1 or l2:
            if l1 == [] or l2 == []:
                m = m + l1 + l2
                break
            if l1[0] < l2[0]:
                m.append(l1.pop(0))
            else:
                m.append(l2.pop(0))
        return m

    mid_idx = (len(lst) - 1) // 2 + 1
    return merge(sort0(lst[0: mid_idx]), sort0(lst[mid_idx:]))


def sort1(lst):
    """Insertion sort"""
    if len(lst) == 1:
        return lst

    def insert(lst, value):
        """Inserts a value to a sorted list"""
        for i in range(len(lst)):
            if value >= lst[i] and (i == len(lst) - 1 or value < lst[i + 1]):
                lst.insert(i + 1, value)
                return lst
        return [value] + lst

    return insert(sort1(lst[1:]), lst[0])


if __name__ == "__main__":
    print(sort1([200, 1, 50, 10, 2, 3, 4, 120]))
