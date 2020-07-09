#!/usr/bin/python
import datetime
import platform
import socket
import subprocess
import sys
from collections import defaultdict
from concurrent.futures.thread import ThreadPoolExecutor
from functools import wraps
from multiprocessing.pool import Pool
import ipaddress


def timer(name):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("-" * 10 + name + "-" * 10)
            start = datetime.datetime.now()
            result = func(*args, **kwargs)
            end = datetime.datetime.now()
            print(f"耗时：{end - start}")
            print("-" * 10 + name + "-" * 10)
            return result

        return wrapper
    return decorate

def test_scan_ports():
    ip = '127.0.0.1'
    test = PMap(ip)
    # 多线程

    print(test.multi_threads(4, 'self.scan_port', range(1083, 3307)))

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

    print(test.multi_process(4, 'self.scan_port', range(1083, 3307)))

def test_scan_ips():
    ip = '127.0.0.1'
    test = PMap(ip)
    # 多线程

    print(test.multi_threads(4, 'self.scan_port', range(1083, 3307)))

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

    print(test.multi_process(4, 'self.scan_port', range(1083, 3307)))

class PMap:
    def agent_call(self, params):
        params_map, result = self.handle_params(params), None
        print(type(params_map))
        n = int(params_map['-n']) if params_map['-n'] else 4
        m = 'self.multi_process' if (params_map['-m'] and params_map['-m']=='proc') else 'self.multi_threads'
        if params_map['-f'] == 'tcp':
            if params_map['-ip']:
                temp = f"{m}(n, 'self.scan_port', [(params_map['-ip'], port) for port in range(1083, 3307)])"
                result = eval(m + r"(n, 'self.scan_port', [(params_map['-ip'], port) for port in range(1083, 3307)])")
        elif params_map['-f'] == 'ping':
            if params_map['-ip']:
                ips = params_map['-ip']
                ips = self.handle_ips(ips)
                result = eval(m + "(n, 'self.ping', ips)")
        if params_map['-w']:
            self.save_to_file(result, params_map['-w'])
        return result

    def ping(self, ip):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        timeout = '-t' if platform.system().lower() == 'darwin' else '-w'
        command = ['ping', param, '1', ip, timeout, '1']
        return ip if not subprocess.call(command) else None

    def scan_port(self, address):
        try:
            s = socket.create_connection(address, 0.0000000000002)
            s.close()
            return str(address[1])
        except socket.error as e:
            pass
            # print(f"{port} is closed on server {self.host}\n")

    def save_to_file(self, result, file_path):
        """
        :param result: string content to write to file
        :param file_path:
        :return: None
        """
        with open(file_path, 'w') as f:
            f.write(" | ".join(str(line) for line in result))

    @timer("多线程")
    def multi_threads(self, n, f, seed):
        with ThreadPoolExecutor(n) as pool:
            result = pool.map(eval(f), seed)
        return list([i for i in result if i])

    @timer("多进程")
    def multi_process(self, n, f, seed):
        pool = Pool(n)
        result = pool.map(eval(f), seed)
        pool.close()
        pool.join()
        return list([i for i in result if i])

    def handle_params(self, params):
        # the length should be odd add the module itself
        params_map = defaultdict(str)
        if len(params) % 2 == 0:
            print("Please check your params!")
            exit(-1)
        for item in [(params[i], params[i + 1]) for i in range(1, len(params) - 1, 2)]:
            params_map[item[0]] = item[1]
        return params_map

    def handle_ips(self, ips):
        ips = ips.split("-")
        if len(ips) == 1:
            return [ips[0]]
        try:
            start_ip, end_ip = ipaddress.IPv4Address(ips[0]), ipaddress.IPv4Address(ips[1])
            return [str(ipaddress.IPv4Address(ip)) for ip in range(int(start_ip), int(end_ip)+1)]
        except ipaddress.AddressValueError:
            print("Please check the given ips")
            exit(-1)


if __name__ == "__main__":
    # test_funcs()
    # params = sys.argv
    params = ['pmap.py', '-n', '5', '-f', 'tcp', '-ip', '127.0.0.1', '-w', 'result.json']
    # params = ['pmap.py', '-n', '5', '-f', 'ping', '-ip', '172.22.34.237-172.22.34.242', '-w', 'result.json', '-m', 'proc']
    test = PMap()
    print(test.agent_call(params))




