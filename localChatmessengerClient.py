import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = "./local_chat_messenger_file"
address = "./local_chat_messenger_client_file"

message = b"Message to send to the client"

os.remove(address)
sock.bind(address)

try:
    print("sending {!r}".format(message))
    sent = sock.sendto(message, server_address)
    print("waiting to receive")
    data, server = sock.recvfrom(4060)

    print("received {!r}".format(data.decode()))

finally:
    print("closing socket")
    sock.close()