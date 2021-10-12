from homework9.task1 import merge_sorted_files


file_list1 = ['file1.txt', 'file2.txt', 'file3.txt']

def test_merge_sorted_files_3_files():
    assert(list(merge_sorted_files(file_list1)) == [1,2,3,4,5,6,7,8,9])


file_list2 = ['file3.txt', 'file4.txt']

def test_merge_sorted_files_2_files_dif_length():
    assert(list(merge_sorted_files(file_list2)) == [5,7,8,9,10,11,12])
