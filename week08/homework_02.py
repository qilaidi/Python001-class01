"""
作业二：
自定义一个 python 函数，实现 map() 函数的功能。
"""


def fake_map(func, *iter_thing):
    iter_thing = zip(*iter_thing)
    for item in iter_thing:
        try:
            yield func(*item)
        except TypeError:
            yield func(item)


def test_fake_map_1(num):
    return num * 2


def test_fake_map_2(arg1, arg2):
    print(f"{arg1}, {arg2}!")


def test_fake_map_3(arg1, arg2, arg3):
    print(f"{arg1}, {arg2}{arg3}")


if __name__ == '__main__':
    print(list(fake_map(test_fake_map_1, [1, 2, 3])))
    list(fake_map(test_fake_map_2, ["hello", "你好"], ["world", "世界"]))
    list(fake_map(test_fake_map_3, ["hello", "你好"], ["world", "世界"], ["!", "！"]))
