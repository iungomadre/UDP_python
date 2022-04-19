import socket
import argparse


# UDP server. Change the functionality by modifying self._utilize_data()
class UDPServer:
    def __init__(self, host: str, port: int, buffer_size: int):
        self._host = host
        self._port = port
        self._buffer_size = buffer_size
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __enter__(self):
        self._socket.bind((self._host, self._port))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._socket.close()

    def start(self):
        while True:
            data_address = self._socket.recvfrom(self._buffer_size)
            data = data_address[0]
            address = data_address[1]
            self._utilize_data(data, address)

    def _utilize_data(self, data: bytes, address: tuple):
        # prints received bytes
        print(f"from {address[0]}:{address[1]} -> {data}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Start UDP server receiving data from senders")
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    parser.add_argument("buffer_size", type=int)
    args = parser.parse_args()

    with UDPServer(args.host, args.port, args.buffer_size) as serv:
        if __debug__:
            print(f"Server has successfully started at {args.host}:{args.port}")
            print("receiving...")
        serv.start()
