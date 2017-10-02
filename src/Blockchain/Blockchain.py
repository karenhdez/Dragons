from Block import *


class Blockchain(object):

    def __init__(self):

        self.__first = None
        self.__size = 0


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        pass


    def addBlock(self, r):

        new = Block(r)

        if self.__first == None:
            self.__first = new
        else:
            self.__first.next = new

        self.__size += 1


    def getBlock(self, i):

        n = self.__first
        while not n == None:
            if i > 0:
                n = n.next
                i -= 1
            else:
                return n.data


    # TODO
    def checkBlockExists(self):

        return


    # TODO
    def getValidation(self):

        return


    def getRecordsByPatient(self, firstName, lastName):

        results = Blockchain()

        i = 0
        n = self.getBlock(i)
        s = self.size()
        while i < s:
            if n.getFirstName() == firstName and n.getLastName() == lastName:
                results.addBlock(n)
            i += 1

        return results


    def getRecordsBySSN(self, SSN):

        results = Blockchain()

        i = 0
        n = self.getBlock(i)
        s = self.size()
        while i < s:
            if n.getSSN() == SSN:
                results.addBlock(n)
            i += 1

        return results


    def getRecordsByProvider(self, provider):

        results = Blockchain()

        i = 0
        n = self.getBlock(i)
        s = self.size()
        while i < s:
            if n.getProvider() == provider:
                results.addBlock(n)
            i += 1

        return results


    def getRecordsWindow(self, start, end):

        results = Blockchain()

        i = 0
        n = self.getBlock(i)
        s = self.getSize()
        while i < s:
            if n.getTimestamp() == start and n.getTimestamp() == end:
                results.addBlock(n)
            i += 1

        return results


    #TODO
    def getAllRecords(self):

        return


    def printList(self):

        print("Records: ")
        #print(self._list)