import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT =8080

sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sever_socket.bind((SERVER_HOST,SERVER_PORT))

sever_socket.listen(5)

print(f"Listerning on port {SERVER_PORT} ...")