import time


class Logger():
    def __init__(self, serv):
        self.server = serv

    def log(self, msg):
        print(f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} {self.server}] {msg}')