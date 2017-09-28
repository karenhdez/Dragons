


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