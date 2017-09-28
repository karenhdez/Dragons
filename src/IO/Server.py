import socket

from src.Record import *

from src.Blockchain.Blockchain import *


class Server:

    def __init__(self):

        pass


    def generateClientRecord(self, firstName, lastName, ssn, provider):

        return Record(firstName, lastName, ssn, provider)


    def main(self):

        block = Blockchain()

        #try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("", 6019))
        sock.listen(1)

        conn, addr = sock.accept()

        while True:

            option = conn.recv(1024)
            conn.sendall(option)

            if option in ("N", "n"):

                firstName = conn.recv(1024)
                conn.sendall(option)
                lastName = conn.recv(1024)
                conn.sendall(option)
                ssn = conn.recv(1024)
                conn.sendall(option)
                provider = conn.recv(1024)
                conn.sendall(option)

                clientRecord = self.generateClientRecord(firstName, lastName, int(ssn), provider)
                block.addRecord(clientRecord)

                list = block.getListByPatient(firstName, lastName)
                print(list.printList())

            elif option in ("Q", "q"):

                conn.close()
                sock.close()
                break

        # except ValueError:
        #
	     #   print("ValueError")