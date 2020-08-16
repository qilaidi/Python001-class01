"""
作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
"""
import datetime
import functools
from time import sleep


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        starttime = datetime.datetime.now()
        result = func(*args, **kwargs)
        endtime = datetime.datetime.now()
        print(f"函数的运行时间: {endtime - starttime}")
        return result

    return wrapper


@timer
def test_func(sleep_time):
    sleep(sleep_time)
    return sleep_time


if __name__ == '__main__':
    print(test_func(10))
