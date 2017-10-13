import os, io, signal, fcntl
from multiprocessing import Process
from Blockchain.Block import *
from Blockchain.Record import *
from Verifier import *


class Handler:

    def __init__(self):

        self.__pList = []


    def verifyAuthorization(self, p):

        return False


    def printResultAsJSON(self, l):

        return


    def sendUnverifiedBlockToProcesses(self, b, count):

        for i in range(count):

            v = Verifier()

            reader, writer = os.pipe()
            fcntl.fcntl(reader, fcntl.F_SETFL, os.O_NONBLOCK)

            p = Process(target=v.main, args=((b,reader,writer),))
            p.start()

            os.close(writer)
            reader = io.open(reader, 'rb', 0)

            self.__pList.append((p.pid, reader))


    def checkForFinishedProcesses(self):

        solved = False

        while not solved:

            for p in self.__pList:
                reader = p[1]
                solution = reader.read()
                if solution != None:
                    solved = True
                    print("Process " + str(p[0]) + " found " + solution)
                    break


    def killProcesses(self):

        for p in self.__pList:
            os.kill(p[0], signal.SIGTERM)
            #v.processID.join()


    def addVerifiedBlockToBlockchain(self, b):

        return


    def verifyBlockchain(self):

        return False


    def handleNewRecordRequest(self):

        return


    def handleSearchRequest(self):

        return


    def createUnverifiedBlock(self, r):

        return


    def main(self):

        r = Record('a', 'b', 1, 'c')
        b = UnverifiedBlock(r)

        self.sendUnverifiedBlockToProcesses(b, 3)

        print("Waiting for verification")

        self.checkForFinishedProcesses()

        print("Ended verification")

        self.killProcesses()



h = Handler()
h.main()