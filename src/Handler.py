import os, io, signal, fcntl
from Queue import Empty
from multiprocessing import Process, Queue
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

            queue = Queue()
            p = Process(target=v.main, args=((b,queue),))
            p.start()

            #queue.close()
            #queue.join_thread()

            self.__pList.append((p.pid, queue))


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


    def handleNewRecordRequest(self):

        return


    def handleSearchRequest(self):

        return


    def createUnverifiedBlock(self, r):

        return


    def main(self):

        r = Record('a', 'b', 1, 'c')
        b = UnverifiedBlock(r)

        print("Waiting for verification")

        self.sendUnverifiedBlockToProcesses(b, 3)
        self.checkForFinishedProcesses()

        print("Ended verification")

        self.killProcesses()



h = Handler()
h.main()