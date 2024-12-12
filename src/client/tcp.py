import logging
import socket
import os

logger = logging.getLogger(__name__)


def start_tcp_client(host:str,port:int):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.debug("connecting...")
    client.connect((host,port))

    try:
        while True:
            message = input("Enter Message $> ")
            if not message:
                continue
            client.send(message.encode("utf-8"))
            response = client.recv(1024)
            print(f"Server response: {response.decode('utf-8')}")
            if response == b"SEE U LATER ALIGATOR":
                break
    finally:
        client.close()


if __name__ == "__main__":
    host = os.getenv("HOST","localhost")
    start_tcp_client(host=host, port=7777)
