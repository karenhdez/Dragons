import socket
import time


class Client:

    def __init__(self, port):

        self.__menu = self.menuMain
        self.__port = port
        self.__sock = None


    def inputUserInfo(self, msg, type):

        while True:
            info = raw_input(msg)
            try:
                type(info)
                if len(info) > 0:
                    break
            except ValueError:
                print("Try again")

        return info


    def sendData(self, data=" "):

        self.__sock.sendall(data)
        data = self.__sock.recv(1024)
        #print("Received " + data)
        return data


    def menuMain(self):

        print("===================================")
        print("Main Menu")
        print("Please enter an option:")
        print("(N) - New User")
        print("(G) - Get Info")
        print("(Q) - Quit")
        print("===================================")

        option = self.inputUserInfo("", str)
        self.sendData(option)

        if option in ("N", "n"):

            self.__menu = self.menuAdd

        elif option in ("G", "g"):

            self.__menu = self.menuGet

        elif option in ("Q", "q"):

            self.__sock.close()
            return False

        return True


    def menuAdd(self):

        print("===================================")
        print("Add record module")
        print("(Q) - Quit")
        print("===================================")

        for msg in (
                ("Enter your first name:", str),
                ("Enter your last name:", str),
                ("Enter your social security number:", int),
                ("Enter your medical provider:", str)):

            info = self.inputUserInfo(msg[0], msg[1])
            self.sendData(info)

            if info in ("Q", "q"):

                self.__menu = self.menuMain
                return True

        print(self.sendData())
        print("Record added")

        self.__menu = self.menuMain

        return True


    def menuGet(self):

        print("===================================")
        print("Record Retrieval Module")
        print("Please enter an option:")
        print("(1) - Search by Name")
        print("(2) - Search by Social Security Number")
        print("(3) - Search by Provider")
        print("(Q) - Quit")
        print("===================================")

        record = None

        while True:

            option = self.inputUserInfo("", str)

            try:
                if option in ("Q", "q"):

                    self.sendData(option)
                    self.__menu = self.menuMain
                    return True

                elif int(option) == 1:

                    self.sendData(option)
                    firstName = self.inputUserInfo("Enter first name:", str)
                    self.sendData(firstName)
                    lastName = self.inputUserInfo("Enter last name:", str)
                    self.sendData(lastName)
                    break

                elif int(option) == 2:

                    self.sendData(option)
                    info = self.inputUserInfo("Enter social security number:", int)
                    self.sendData(info)
                    break

                elif int(option) == 3:

                    self.sendData(option)
                    info = self.inputUserInfo("Enter provider:", str)
                    self.sendData(info)
                    break

                print("Invalid option")

            except ValueError:
                print("Invalid option")

        print("===================================")
        print("Record retrieved")
        print("===================================")
        print(self.sendData())
        print("===================================")

        self.__menu = self.menuMain

        return True


    def main(self):

        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.connect(("localhost", self.__port))

        while self.__menu():
            pass