import datetime


class Record:

    def __init__(self, f, l, ssn, p):

        self._next = None

        self.firstName = f
        self.lastName = l
        self.SSN = ssn
        self.provider = p
        self.timestamp = str(datetime.datetime.now()).split('.')[0]


    # TODO: Add more attributes to return
    def toString(self):

        return ""


    def setTimestamp(self, ts):

        self.timestamp = ts


    def getTimestamp(self):

        return self.timestamp


