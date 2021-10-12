"""
Given a dictionary (tree), that can contain multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    occurrences = 0
    values = tree.values() if isinstance(tree, dict) else tree
    for value in values:
        if element == value:
            occurrences += 1
        elif type(value) in (dict, list, tuple, set):
            occurrences += find_occurrences(value, element)
    return occurrences


if __name__ == '__main__':

    print(find_occurrences(example_tree, "RED"))  # 6

    tree1 = {
         "first": ["RED", "BLUE"],
         "second": ("simple", ["RED", "valued"])}

# print(find_occurrences(tree1, "RED"))  #2

