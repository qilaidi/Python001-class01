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


class PMap:
    def agent_call(self, params):
        params_map, result = self.handle_params(params), None
        print(type(params_map))
        n = int(params_map['-n']) if params_map['-n'] else 4
        m = 'self.multi_process' if (params_map['-m'] and params_map['-m']=='proc') else 'self.multi_threads'
        if params_map['-f'] == 'tcp':
            if params_map['-ip']:
                seed = [(params_map["-ip"], port) for port in range(1083, 3307)]
                result = eval(f'{m}(n, "self.scan_port", seed)')
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
    params = sys.argv
    test = PMap()
    print(test.agent_call(params))




