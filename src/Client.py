import socket
import time


class Client:

    def __init__(self):

        pass


    def displayMenu(self):

        print("===================================")
        print("Please Enter an Option:")
        print("(N) - New User")
        print("(G) - Getting Info")
        print("(Q) - Quit")
        print("===================================")


    def getUserOption(self):

        option = ""
        while True:
            option = raw_input("Option:")
            if option in ("N", "n", "Q", "q"):
                break

        return option


    def getUserFirstName(self):

        firstName = ""
        while True:
            firstName = raw_input("Enter your first name:")
            if len(firstName) > 0:
                break

        return firstName


    def getUserLastName(self):

        lastName = ""
        while True:
            lastName = raw_input("Enter your last name:")
            if len(lastName) != 0:
                break

        return lastName


    def getUserSSN(self):

        ssn = ""
        while True:
            ssn = raw_input("Enter your social security number:")
            if len(ssn) > 0:
                break

        return ssn


    def getUserProvider(self):

        provider = ""
        while True:
            provider = raw_input("Enter your medical provider:")
            if len(provider) > 0:
                break

        return provider


    def sendData(self, sock, data):

        sock.sendall(data)
        data = sock.recv(1024)
        print("Received " + data)


    def main(self):

        #try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", 6019))

        while True:

            self.displayMenu()
            option = self.getUserOption()
            self.sendData(sock, option)

            if option in ("N", "n"):

                self.sendData(sock, self.getUserFirstName())
                self.sendData(sock, self.getUserLastName())
                self.sendData(sock, self.getUserSSN())
                self.sendData(sock, self.getUserProvider())

            elif option in ("Q", "q"):

                sock.close()
                break

        #except:

        #    pass