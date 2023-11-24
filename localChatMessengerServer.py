import socket
import os

import faker

class Server:
    @staticmethod
    def start():
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        server_address = "./local_chat_messenger_file"
        try:
            os.unlink(server_address)
        except FileNotFoundError:
            pass
        print("starting up on {}".format(server_address))
        sock.bind(server_address)

        while True:
            print("\nwaiting to receive message")
            data, address = sock.recvfrom(4060)

            print("received {} bytes from {}".format(len(data), address))
            print(data)
            if data:
                personData = PersonData()
                sentData = personData.toString().encode()
                sent = sock.sendto(sentData, address)
                print("sent {} bytes back to {}".format(sent, address))




class PersonData:
    def __init__(self):
        fake = faker.Faker(["ja-JP"])
        self.name = fake.name()
        self.address = fake.address()
        self.text = fake.text()

    def toString(self):
        return ("name: " + self.name + "\naddress: " +
                self.address + "\nmessage: " + self.text)


Server.start()
