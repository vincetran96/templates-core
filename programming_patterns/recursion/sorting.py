"""I think I have to be very careful with how 
Python changes the values inside collections
(e.g., lists, etc.) because ideally functions
that sort a list should not modify the original list

But why do we want sorting functions to _not_ modify 
the original list anyway? One reason can be because
we want to keep the original list as a reference 
after the sort. Another reason can be because we 
want to write functions in as a "pure" manner as possible, 
which means that for each input x, the function should 
only output y, without changing x
"""
from copy import deepcopy
from typing import List


def bubble_sort(lst: List[int]) -> List[int]:
    """I want to write a bubble sort function using
    recursion, instead of looping

    Define an auxiliary func `swap`

    The idea is like so:
      - Use 3 vars: 2 indexes for swapping and a boolean indicating if
        a swap action has been done for one round (one round means one
        trip/loop from the start to end of list)
      - If the right idx is out of bound, and the swap var is True,
        then begin from the start of list; If the swap var is False
        (meaning no swap action has been done for that round), then terminate
      - If the right idx is in-bound, keep checking if swap is needed
        and flip the swap var if a swap action has been done

    Returns:
        A new sorted list

    Args:
        lst: (List[int])
    """
    lst_cp = deepcopy(lst)

    def swap(i_left: int = 0, i_right: int = 1, swapped: bool = False):
        """Swap helper
        """
        if i_right == len(lst_cp):
            if swapped:
                swap()
        else:
            if lst_cp[i_left] > lst_cp[i_right]:
                lst_cp[i_left], lst_cp[i_right] = \
                    lst_cp[i_right], lst_cp[i_left]
                swapped = True
            swap(i_left + 1, i_right + 1, swapped)
    
    if lst_cp:
        swap()
    return lst_cp


def merge_sort(lst: List[int]) -> List[int]:
    """A merge sort function using recursion

    Define 2 auxiliary functions:

    merge:
      - It merges 2 already sorted lists into 1, very simple

    sort:
      - The idea of this function is to divide the list into
        sub-lists until the sub-list reaches length <= 1, at
        which point we return the sub-list
      - To divide, this function recursively calls itself
      - Then finally there is the outermost `merge` call

    Returns:
        A new sorted list

    Args:
        lst: (List[int])
    """
    def _merge(l0: List[int], l1: List[int], result: List[int]):
        """Merges 2 sorted lists into 1
        """
        if not l0 or not l1:
            return result + l1 + l0
        else:
            if l0[0] < l1[0]:
                _in = l0.pop(0)
            else:
                _in = l1.pop(0)
            return _merge(l0, l1, result + [_in])
        
    def _sort(lst_: List[int]):
        """Sorts helper
        
        If the length <= 2, divide it then merge
        """
        if len(lst_) <= 1:
            return lst_
        mid_idx = int((len(lst_) - 1) / 2) + 1
        return _merge(_sort(lst_[0:mid_idx]), _sort(lst_[mid_idx:]), [])
        
    return _sort(lst)


def selection_sort(lst: List[int]) -> List[int]:
    """A selection sort function using recursion

    Define an auxiliary function `sort`

    The idea is like so:
      - Use 2 vars: start index and current index. The
        starting index keeps track of the start of the
        "segment" to do the swapping. The current index keeps
        track of the current element to compare with the element
        at the start of the segment
      - If the element at the current index is less than
        the element at the start, swap them. Keep doing this
        until the current element reaches the end of the segment,
        at which point we move the start index forward and set the
        current index next to it

    Returns:
        A new sorted list

    Args:
        lst: (List[int])
    """
    lst_cp = deepcopy(lst)
    def _sort(start_idx: int = 0, current_idx: int = 1):
        """Sorts helper
        """
        if start_idx < len(lst_cp) - 1:
            if lst_cp[start_idx] > lst_cp[current_idx]:
                lst_cp[start_idx], lst_cp[current_idx] = \
                    lst_cp[current_idx], lst_cp[start_idx]
            if current_idx == len(lst_cp) - 1:
                _sort(start_idx + 1, start_idx + 2)
            else:
                _sort(start_idx, current_idx + 1)

    if len(lst_cp) > 1:
        _sort()
    return lst_cp


if __name__ == "__main__":
    print("Bubble sort:")
    print(bubble_sort([3,2,1]))
    print(bubble_sort([1]))
    print(bubble_sort([]))
    print("Merge sort:")
    print(merge_sort([1000,1,5,3,7000,15,2]))
    print(merge_sort([1]))
    print(merge_sort([]))
    print("Selection sort:")
    print(selection_sort([1000,1,5,3,7000,15,2]))
    print(selection_sort([1000,1,-5,3,7000,15,2]))
    print(selection_sort([1]))
    print(selection_sort([]))
