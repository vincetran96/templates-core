from typing import List


def bubble_sort(lst: List):
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
        if i_right == len(lst):
            if swapped:
                swap()
        else:
            if lst[i_left] > lst[i_right]:
                lst[i_left], lst[i_right] = lst[i_right], lst[i_left]
                swapped = True
            swap(i_left + 1, i_right + 1, swapped)
    
    swap()
    return lst


if __name__ == "__main__":
    print(bubble_sort([3,2,1]))
