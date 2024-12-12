import socket
import logging
import os

logger = logging.getLogger(__name__)

def handle_client(client_socket:socket.socket, client_address:str):
    print(f"Connection established with {client_address}")

    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                continue
            message = message.decode("utf-8")
            print(f"Recieved message: '{message}'")
            if message == "QUIT":
                client_socket.sendto("SEE U LATER ALIGATOR".encode("utf-8"), client_address)
                break
            client_socket.sendto(f"Just to know I have recieved this message: {message}".encode("utf-8"), client_address)
    except Exception as exc:
        logger.error("Error handling message", exc_info=exc)
    finally:
        client_socket.close()

def start(host:str="0.0.0.0", port:int=7777):
    instance:socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("TCP Socket instanciated")
    instance.bind((host,port))
    print(f"Address {host} on port {port} bound to socket")

    instance.listen(10)
    print(f"Server started on {host}:{port}")

    while True:
        client_socket, client_address = instance.accept()
        handle_client(client_socket,client_address)


if __name__ == "__main__":
    host = os.getenv("HOST", "localhost")
    start(host=host)
