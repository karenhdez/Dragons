import os, time, random


class Verifier:

    def __init__(self):

        self.__credits = 0
        self.__UB = ""
        self.__result = None


    def tryVerifyingBlock(self, b, reader, writer):

        os.close(reader)
        writer = os.fdopen(writer, 'w')

        while not self.trySolvingWork(b):
            pass

        writer.write(self.__result)
        writer.close()


    def trySolvingWork(self, b):

        i = random.randint(1, 1000000)
        if i == 3:
            self.__result = "solution"
            return True

        return False


    def workSolved(self):

        return self.__result != None


    def produceGuess(self):

        return


    def generateUB(self):

        return


    def verifyBlock(self, b):

        return


    def checkBlockExists(self, b):

        return


    def checkBlockVerified(self, b):

        return


    def main(self, args):

        print("Started process " + str(os.getpid()))

        b = args[0]
        reader = args[1]
        writer = args[2]

        self.tryVerifyingBlock(b, reader, writer)



class Work:

    def __init__(self):

        self.solved = False


    def puzzle(self):

        return False