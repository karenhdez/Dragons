

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next



class LinkedList:

    def __init__(self):

        self.first = None


    def size(self):

        s = 0
        n = self.first
        while not n == None:
            s += 1
            n = n.next

        return s


    def add(self, data):

        new = Node(data)

        if self.first == None:
            self.first = new
        else:
            self.first.next = new


    def get(self, i):

        n = self.first
        while not n == None:
            if i > 0:
                n = n.next
                i -= 1
            else:
                return n.data


    def printList(self):

        n = self.first
        while not n == None:
            print(n.data.toString())
            n = n.next



class Blockchain(object):

    def __init__(self):

        self._list = LinkedList()


    def addRecord(self, r):

        self._list.add(r)


    def getList(self):

        return self._list


    def getListByPatient(self, firstName, lastName):

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


    def getListByProvider(self, provider):

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


    def getListByDateWindow(self, start, end):

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


    def printList(self):

        print("Records: ")
        print(self._list)