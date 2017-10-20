import socket
from src.Blockchain.Record import *
from src.Handler import Handler


class Server:

    def __init__(self):

        self.__handler = Handler()
        self.__menu = self.menuMain
        self.__port = None
        self.__sock = None
        self.__conn = None
        self.__addr = None


    @property
    def port(self):
        return self.__port

    # Setters
    @port.setter
    def port(self, val):
        pass


    def addClientRecord(self, firstName, lastName, ssn, provider):

        self.__handler.handleNewRecordRequest(firstName, lastName, ssn, provider)

        #while not self.__handler.finished:
        #    pass


    def getClientRecord(self, firstName, lastName, ssn, provider):

        #list = self.__handler.handleSearchRequest(firstName, lastName, ssn, provider)
        return "INFO"


    def sendData(self, msg=" "):

        data = self.__conn.recv(1024)
        self.__conn.sendall(msg)
        return data


    def menuMain(self):

        option = self.sendData()

        if option in ("N", "n"):

            self.__menu = self.menuAdd

        elif option in ("G", "g"):

            self.__menu = self.menuGet

        elif option in ("Q", "q"):

            self.__conn.close()
            self.__sock.close()
            return False

        return True


    def menuAdd(self):

        values = []

        for i in range(4):

            data = self.sendData()

            if data in ("Q", "q"):
                self.__menu = self.menuMain
                return True

            values.append(data)

        firstName = values[0]
        lastName = values[1]
        ssn = int(values[2])
        provider = values[3]

        self.addClientRecord(firstName, lastName, ssn, provider)

        self.sendData()

        self.__menu = self.menuMain

        return True


    def menuGet(self):

        option = self.sendData()

        firstName = None
        lastName = None
        ssn = None
        provider = None

        if option in ("Q", "q"):

            self.__menu = self.menuMain
            return True

        elif int(option) == 1:

            firstName = self.sendData()
            lastName = self.sendData()

        elif int(option) == 2:

            ssn = self.sendData()

        elif int(option) == 3:

            provider = self.sendData()


        info = self.getClientRecord(firstName, lastName, ssn, provider)
        self.sendData(info)

        self.__menu = self.menuMain

        return True


    def main(self):

        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.bind(("", 0))
        self.__port = self.__sock.getsockname()[1]
        self.__sock.listen(1)

        self.__conn, self.__addr = self.__sock.accept()

        while self.__menu():
            pass