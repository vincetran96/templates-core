"""If you run this script in its current dir, Python will complain:
ModuleNotFoundError: No module named 'programming_patterns'

One way to run the main function in this file is to create a .py
file at the root dir of this project, with the following content:

```
from programming_patterns.namespaces.import_modules import main


main()
```
"""
from programming_patterns.recursion.sorting import merge_sort


def main():
    print(merge_sort([1000, 500, 20]))


if __name__ == "__main__":
    main()
