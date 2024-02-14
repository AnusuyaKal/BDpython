import socket

class NetworkConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __enter__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        return self.socket

    def __exit__(self, exc_type, exc_value, traceback):
        if self.socket:
            self.socket.close()

# Example usage
host = 'example.com'
port = 80

# Using the context manager to establish a network connection
with NetworkConnection(host, port) as conn:
    conn.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    response = conn.recv(4096)
    print(response.decode('utf-8'))

# The network connection is automatically closed when exiting the 'with' block
