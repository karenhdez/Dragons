from LinkedList import *
import jwt


class Blockchain:

    def __init__(self):

        self._list = LinkedList()


    def addBlock(self, r):

        self._list.add(r)


    # TODO
    def checkBlockExists(self):

        return


    # TODO
    def getBlock(self):

        return


    # TODO
    def getValidation(self):

        return


    def getRecordsByPatient(self, firstName, lastName):

        l = self._list
        results = LinkedList()

        i = 0
        n = l.get(i)
        s = l.size()
        while i < s:
            if n.getFirstName() == firstName and n.getLastName() == lastName:
                results.add(n)
            i += 1

        return results


    def getRecordsBySSN(self, SSN):

        l = self._list
        results = LinkedList()

        i = 0
        n = l.get(i)
        s = l.size()
        while i < s:
            if n.getSSN() == SSN:
                results.add(n)
            i += 1

        return results


    def getRecordsByProvider(self, provider):

        l = self._list
        results = LinkedList()

        i = 0
        n = l.get(i)
        s = l.size()
        while i < s:
            if n.getProvider() == provider:
                results.add(n)
            i += 1

        return results


    def getRecordsWindow(self, start, end):

        l = self._list
        results = LinkedList()

        i = 0
        n = l.get(i)
        s = l.size()
        while i < s:
            if n.getTimestamp() == start and n.getTimestamp() == end:
                results.add(n)
            i += 1

        return results


    #TODO
    def getAllRecords(self):

        return


    def printList(self):

        print("Records: ")
        print(self._list)