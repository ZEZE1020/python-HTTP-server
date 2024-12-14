import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT =8095

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER_HOST,SERVER_PORT))

server_socket.listen(5)

print(f"Listening on port {SERVER_PORT} ...")

client_socket, client_address = server_socket.accept()
print(client_socket)
print(client_address)