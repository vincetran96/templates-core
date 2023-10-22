from typing import List


def find_max(lst: List[int]) -> int:
    '''Finds largest int in list

    Raises an IndexError if the list is empty
    '''
    def find(last_val: int, idx: int = 0) -> int:
        '''Finder helper
        '''
        if lst[idx] > last_val:
            last_val = lst[idx]
        if idx == len(lst) - 1:
            return last_val
        return find(last_val, idx + 1)

    return find(lst[0])


if __name__ == "__main__":
    print(find_max([-1, -20, -3]))
    print(find_max([-1, -20, 3]))
    print(find_max([0]))
    print(find_max([]))
