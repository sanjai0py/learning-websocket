import socket

class TCPServer:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 5
    server_address = ("127.0.0.1", 3000)
    allow_reuse_address = False
    allow_reuse_port = False

    def __init__(self, bind_and_activate=True):
        self.sock = socket.socket(self.address_family, self.socket_type)
        if bind_and_activate:
            try:
                self.server_bind()
                self.server_activate()
            except:
                self.sock.close()
                raise

    def server_bind(self):
        if self.allow_reuse_address and hasattr(socket, "SO_REUSEADDR"):
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if self.allow_reuse_port and hasattr(socket, "SO_REUSEPORT"):
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.sock.bind(self.server_address)
        self.server_address = self.sock.getsockname()

    def server_activate(self):
        self.sock.listen(self.request_queue_size)
        print("Listening at", self.sock.getsockname())

        while True:
            (conn, addr) = self.sock.accept()
            print("Connected by", addr)

            # For the sake of this tutorial,
            # we're reading just the first 1024 bytes sent by the client.
            data = conn.recv(1024)

            response = self.handle_request(data)

            conn.sendall(response)
            conn.close()

    def handle_request(self, data):
        return data
