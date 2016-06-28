import socket
import appcodec
from time import sleep
from struct import *


class TelemeterRcDaemon():
    """docstring for TelemeterRcDaemon"""
    def __init__(self, src, dst):
        self.src = bytes(bytearray.fromhex(src))
        self.dst = bytes(bytearray.fromhex(dst))
        self.type = socket.htons(257)
        self.socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
        self.socket.bind(("eth0", 0))
        print(self.socket)

    def sendFrame(self, payload):
        assert(len(self.src) == len(self.dst) == 6)
        assert(len(self.type) == 2)
        return self.socket.send(self.dst + self.src + self.type + payload)

    def push(self):
        while 1:
            payload = appcodec.encode()
            self.sendFrame(payload)
            sleep(.01)
            print(payload.decode("utf-8") + " sent")

    def listen(self):
        #self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        #self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        while(1):
            frame = self.socket.recv(2048)
            print(frame)
            if(frame[12:14] == self.type):
                self.decode(frame[14: ])

    def decode(self, frame):
        appcodec.decode(frame)
