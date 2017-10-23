import os, time, random


class Verifier:

    def __init__(self):

        self.__credits = 0
        self.__UB = ""
        self.__result = None


    def tryVerifyingBlock(self, b, queue):


        while not self.trySolvingWork(b):
            pass

        queue.put(self.__result)


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
        queue = args[1]

        self.tryVerifyingBlock(b, queue)



class Work:

    def __init__(self):

        self.solved = False


    def puzzle(self):

        return False