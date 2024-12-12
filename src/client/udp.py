import logging
import socket
import os

logger = logging.getLogger(__name__)


def start_tcp_client(host:str,port:int):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        while True:
            message = input("Enter Message $> ")
            if not message:
                continue
            client.sendto(message.encode("utf-8"), (host,port))
            response, _ = client.recvfrom(1024)
            print(f"Server response: {response.decode('utf-8')}")
            if message == "QUIT":
                break
    finally:
        client.close()


if __name__ == "__main__":
    host=os.getenv("HOST","localhost")
    start_tcp_client(host=host, port=8888)
