# We have a file that works as key-value storage, each line is represented
# as key and value separated by = symbol, example:
#
# name=kek last_name=top song_name=shadilay power=9001
#
# Values can be strings or integer numbers. If a value
# can be treated both as a number and a string, it is treated as number.
#
# Write a wrapper class for this key value storage that works like this:
#
# storage = KeyValueStorage('path_to_file.txt')
# that has its keys and values accessible as collection items and as attributes.
# Example: storage['name'] # will be string 'kek'
# storage.song_name # will be 'shadilay' storage.power # will be integer 9001
#
# In case of attribute clash existing built-in attributes take precedence.
# In case when value cannot be assigned to an attribute (for example when there's a line 1=something)
# ValueError should be raised. File size is expected to be small, you are permitted to read it entirely into memory.

class KeyValueStorage:
    def __init__(self, path):
        self.path = path
        dict_line = {}
        with open('hw8_task1_data.txt') as f:
            for line in f.readlines():
                lst = line.split("=")
                s = ".,:;!*-+()/#%&"
                for char in s:
                    if char in lst[0] or lst[0][0] is int:
                        print("wrong symbol in the attribute", lst[0])
                        raise ValueError
                    else:
                        pass
                dict_line[lst[0]] = lst[1]
                setattr(self, lst[0], lst[1])

    def __getitem__(self, key):
        return self.__dict__[key]


if __name__ == '__main__':

    storage = KeyValueStorage('hw8_task1_data.txt')
    print(storage['name'])
    print(storage.name)
    # print(storage.power)
