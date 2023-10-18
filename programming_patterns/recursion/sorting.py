from typing import List


def bubble_sort(lst: List[int]):
    '''I want to write a bubble sort function using recursion,
    instead of looping
    
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

    The sort is done in-place of the list
    '''
    def swap(i_left: int=0, i_right: int=1, swapped: bool=False):
        '''Swap helper
        '''
        if i_right == len(lst):
            if swapped:
                swap()
        else:
            if lst[i_left] > lst[i_right]:
                lst[i_left], lst[i_right] = lst[i_right], lst[i_left]
                swapped = True
            swap(i_left + 1, i_right + 1, swapped)
    
    if lst:
        swap()
    return lst


def merge_sort(lst: List[int]):
    '''A merge sort function using recursion

    Define 2 auxiliary functions:
    
    1. merge: It merges 2 already sorted lists into 1, very simple
    2. sort:
        - The idea of this function is to divide the list into
        sub-lists until the sub-list reaches length <= 1, at
        which point we return the sub-list
        - To divide, this function recursively calls itself
        - Then finally there is the outer-most `merge` call

    Returns a new sorted list
    '''
    def merge(l0: List[int], l1: List[int], result: List[int]):
        '''Merges 2 sorted lists into 1
        '''
        if not l0 or not l1:
            return result + l1 + l0
        else:
            if l0[0] < l1[0]:
                _in = l0.pop(0)
            else:
                _in = l1.pop(0)
            return merge(l0, l1, result + [_in])
        
    def sort(lst_: List[int]):
        '''Sorts helper
        
        If the length <= 2, divide it then merge
        '''
        if len(lst_) <= 1:
            return lst_
        mid_idx = int((len(lst_) - 1) / 2) + 1
        return merge(sort(lst_[0:mid_idx]), sort(lst_[mid_idx:]), [])
        
    return sort(lst)


if __name__ == "__main__":
    print(bubble_sort([3,2,1]))
    print(bubble_sort([1]))
    print(bubble_sort([]))
    print(merge_sort([1000,1,5,3,7000,15,2]))
    print(merge_sort([1]))
    print(merge_sort([]))
