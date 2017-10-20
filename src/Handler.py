import os, io, signal
from Queue import Empty
from multiprocessing import Process, Queue
from Blockchain.Blockchain import *
from Blockchain.Block import *
from Blockchain.Record import *
from Verifier import *


class Handler:

    def __init__(self):

        self.__blockchain = Blockchain()
        self.__pList = []
        self.__finished = False


    @property
    def finished(self):
        return self.__finished

    # Setters
    @finished.setter
    def finished(self, val):
        pass


    def verifyAuthorization(self, p):

        return False


    def printResultAsJSON(self, l):

        return


    def createUnverifiedBlock(self, r):

        return UnverifiedBlock(r)


    def sendUnverifiedBlockToProcesses(self, b):

        count = 3

        print()
        print("Waiting for verification")

        for i in range(count):

            v = Verifier()

            queue = Queue()
            p = Process(target=v.main, args=((b,queue),))
            p.start()

            self.__pList.append((p.pid, queue))

        self.checkForFinishedProcesses()

        print("Ended verification")

        self.killProcesses()


    def checkForFinishedProcesses(self):

        solved = False

        while not solved:

            for p in self.__pList:
                queue = p[1]

                solution = None
                try:
                    solution = queue.get_nowait()
                except Empty:
                    pass#print('no output yet')
                else:
                    if solution is not None:
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


    def handleNewRecordRequest(self, firstName, lastName, ssn, provider):

        self.__finished = False

        r = Record(firstName, lastName, ssn, provider)

        b = self.createUnverifiedBlock(r)
        b = self.sendUnverifiedBlockToProcesses(b)
        self.addVerifiedBlockToBlockchain(b)

        self.__finished = True


    def handleSearchRequest(self, firstName, lastName, ssn, provider):

        if not None in (firstName, lastName):
            return self.__blockchain.getRecordsByPatient(firstName, lastName)
        elif ssn is not None:
            return self.__blockchain.getRecordsBySSN(ssn)
        elif provider is not None:
            return self.__blockchain.getRecordsByProvider(provider)