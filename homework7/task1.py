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

occurrences = 0

def find_occurrences(tree: dict, element: Any) -> int:
    global occurrences

    for value in tree.values():
        if type(value) == (str or int or bool):
            if element == value:
                occurrences += 1
        elif type(value) == dict:
            print(type(value))
            tree1 = value
            find_occurrences(tree1, element)
        else:
            repeat = True
            while repeat:
                if (type(value) == list or tuple or set):    # and (type(value) != str):
                    for val in value:
                        if val == value[-1]: repeat = False
                        if type(val) == dict:
                            repeat = False
                            find_occurrences(val, element)
                        elif (type(val) == list) and (type(val) != str):
                            find_occurrences(dict(enumerate(val)), element)
                        elif element == val:
                            occurrences += 1
                            print(occurrences)

    return occurrences


if __name__ == '__main__':

    # print(find_occurrences(example_tree, "RED"))  # 6

    tree1 = {
         "first": ["RED", "BLUE"],
         "second": ("simple", ["RED", "valued"])}

    # print(find_occurrences(tree1, "RED"))  #2

