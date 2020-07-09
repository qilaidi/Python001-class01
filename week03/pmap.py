import datetime
import platform
import socket
import subprocess
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing.pool import Pool


class PMap:
    def __init__(self, host):
        self.host = host

    def __call__(self, *args, **kwargs):
        pass

    def ping(self, ip):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', ip]
        return ip if not subprocess.call(command) else None

    def scan_port(self, port):
        try:
            s = socket.create_connection((self.host, port), 2)
            s.close()
            return port
        except socket.error as e:
            pass
            # print(f"{port} is closed on server {self.host}")

    def save_to_file(self, result, file_path):
        """
        :param result: string content to write to file
        :param file_path:
        :return: None
        """
        with open(file_path, 'w') as f:
            f.write(result)

    def multi_threads(self, n, f, seed):
        with ThreadPoolExecutor(n) as pool:
            result = pool.map(eval(f), seed)
        return list([i for i in result if i])

    def multi_process(self, n, f, seed):
        pool = Pool(n)
        result = pool.map(eval(f), seed)
        pool.close()
        pool.join()
        return list([i for i in result if i])




if __name__ == "__main__":
    ip = '127.0.0.1'
    test = PMap(ip)
    # 多线程
    print("-"*10 + "多线程开始" + "-"*10)
    start = datetime.datetime.now()
    print(test.multi_threads(4, 'self.scan_port', range(1083, 3307)))
    end = datetime.datetime.now()
    print(end - start)
    print("-" * 10 + "多线程结束" + "-" * 10)

    # 单线程
    print("-" * 10 + "单线程开始" + "-" * 10)
    start = datetime.datetime.now()
    result = []
    for i in range(1083, 3307):
        res = test.scan_port(i)
        if res:
            result.append(res)
    print(result)
    end = datetime.datetime.now()
    print(end - start)
    print("-" * 10 + "单线程结束" + "-" * 10)

    # 多进程
    print("-" * 10 + "多进程开始" + "-" * 10)
    start = datetime.datetime.now()
    print(test.multi_process(4, 'self.scan_port', range(1083, 3307)))
    end = datetime.datetime.now()
    print(end - start)
    print("-" * 10 + "多进程结束" + "-" * 10)