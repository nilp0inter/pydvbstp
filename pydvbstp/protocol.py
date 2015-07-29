import asyncio
import socket

from .unpacker import unpack
from .collector import Collector

BIND_ADDR = '0.0.0.0'
MULTICAST_ADDR = '224.0.0.0'


class DVBSTP(asyncio.DatagramProtocol):
    def __init__(self, *args, **kwargs):
        self.bind_addr = BIND_ADDR
        self.multicast_addr = MULTICAST_ADDR
        self.collector = Collector()
        super().__init__(*args, **kwargs)

    @classmethod
    def listener(cls, bind_addr, multicast_addr):
        def factory(*args, **kwargs):
            self = cls(*args, **kwargs)
            self.bind_addr = bind_addr
            self.multicast_addr = multicast_addr
            return self
        return factory

    def connection_made(self, transport):
        sock = transport.get_extra_info('socket')
        membership = (socket.inet_aton(self.multicast_addr) +
                      socket.inet_aton(self.bind_addr))

        sock.setsockopt(socket.IPPROTO_IP,
                        socket.IP_ADD_MEMBERSHIP,
                        membership)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def datagram_received(self, data, addr):
        section = unpack(data)
        new_segment = self.collector.add_section(section)
        if new_segment is not None:
            self.handle_segment(new_segment)

    def handle_segment(self, segment):
        raise NotImplementedError()
