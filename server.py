import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = "1234"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(IP, PORT)

server_socket.listen()

socket_list = [server_socket]

clients = {}
print(f"listening for connections of {IP}:{PORT}...")

def recv_msg(client_socket):
    try:
        msg_hdr = client_socket.recv(HEADER_LENGTH)
        if not len(msg_hdr):
            return False
        msg_len = int(msg_hdr.decode("utf-8").strip())
        return {'header':msg_hdr, 'data':client_socket.recv(msg_len)}

    except:
        return False


