from homework7.task1 import find_occurrences

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

def test_find_occurrences():
    assert(find_occurrences(example_tree, "RED") == 6)


ocurrences = 0

tree1 = {
    "first": ["RED", "BLUE"],
    "second": ("simple", ["RED", "valued"])}

def test_find_occurrences1():
    assert(find_occurrences(tree1, "RED") == 8)    # 6+2