from homework7.task2 import backspace_compare


def test_backspace_compare_simple_case():
    s1 = "ab#c"
    t1 = "ad#c"
    assert(backspace_compare(s1, t1) == True)


def test_backspace_compare_case2():
    s2 = "a##c"
    t2 = "#a#c"
    assert(backspace_compare(s2, t2) == True)


def test_backspace_compare_case3():
    s3 = "aaaaa#####c"
    t3 = "aa##c"
    assert(backspace_compare(s3, t3) == True)


def test_backspace_compare_different_length():
    s3 = "a#c"
    t3 = "b"
    assert(backspace_compare(s3, t3) == False)
