from tcpserver import TCPServer
import socket


class HttpServer(TCPServer):
    def handle_request(self, data):
        response_line = b"HTTP/1.1 200 OK\r\n"
        blank_line = b"\r\n"
        response_body = b"call me!"

        return b"".join([response_line, blank_line, response_body])
