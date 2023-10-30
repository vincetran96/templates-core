"""Misc utils
"""

def flatten_list(lst):
    """Flattens a nested list, with any level
    """
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened
