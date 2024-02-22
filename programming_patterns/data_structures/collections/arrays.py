"""Arrays containing integers
"""
from typing import List


def split_iv(lst: List, fn: bool):
    """Splits lst by a predicate `fn` using the index and the value;
    Behaves like string split: if predicate is True, split at that location

    Args:
        fn: (i, v) -> bool: function taking index, value and returns bool
    """
    sub_lists = []
    candidate = []
    for i, value in enumerate(lst):
        if not fn(i, value):
            candidate.append(value)
        else:
            sub_lists.append(candidate)
            candidate = []
    if candidate:
        sub_lists.append(candidate)

    return sub_lists


if __name__ == "__main__":
    flowerbed = [1, 0, 1, 0, 0, 0, 0, 1]
    sub_lists = split_iv(
        flowerbed,
        lambda i, v:
            v == 1
            or flowerbed[max(0, i-1)] == 1
            or flowerbed[min(len(flowerbed)-1, i+1)] == 1
    )
    print(sub_lists)
