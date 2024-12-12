import socket
import logging
import os

logger = logging.getLogger(__name__)


def handle_client(server_socket:socket.socket):
    while True:
        msg, addr = server_socket.recvfrom(1024)
        if not msg:
            continue
        msg = msg.decode("utf-8")
        print(f"Message received from {addr}: {msg}")
        if msg == "QUIT":
            server_socket.sendto(f"GOODBYE".encode("utf-8"), addr)
            continue
        server_socket.sendto(f"It's ok! I've received: {msg}".encode("utf-8"), addr)

def start_server(host:str="0.0.0.0", port:int=8888):
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server.bind((host,port))
    print(f"Server started on {host}:{port}")

    handle_client(server)


if __name__ == "__main__":
    host = os.getenv("HOST", "localhost")
    start_server(host=host)
