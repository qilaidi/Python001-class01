"""
作业一：

区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

list
tuple
str
dict
collections.deque
"""

# 扁平序列：只能放一种数据类型的序列
# 容器序列：能放各种数据类型的序列
# str 是扁平序列
# list, tuple, dict, collections.deque 是容器序列

import collections


def is_editable(obj):
    try:
        obj.__getattribute__("__setitem__")
        print(f"{obj.__class__.__name__} is mutable")
    except AttributeError:
        print(f"{obj.__class__.__name__} is immutable")


# 可变序列 list:
example_list = [1, 2, 3, 4, 5]
example_tuple = (1, 2, 3, 4, 5)
example_str = "hello string"
example_dict = {"a": 1, "b": 2, "c": 3}
example_deque = collections.deque(example_tuple)

is_editable(example_list)
is_editable(example_tuple)
is_editable(example_str)
is_editable(example_dict)
is_editable(example_deque)

"""
执行结果：
list is mutable
tuple is immutable
str is immutable
dict is mutable
deque is mutable
"""