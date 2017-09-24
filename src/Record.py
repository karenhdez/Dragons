import datetime


class Record:

    def __init__(self, f, l, ssn, p):

        self._next = None

        self._firstName = f
        self._lastName = l
        self._SSN = ssn
        self._provider = p
        self._blockID = self.generateBlockID()
        self._SHA256String = self.generateSHA256()
        self._signedSHA256 = self.generateSignedSHA256()
        self._verificationProcessID = self.generateProcessId()
        self._timestamp = str(datetime.datetime.now()).split('.')[0]


    # Temporary: for now generates random string
    def generateSHA256(self):

        sHA256 = "WELKFRLEA"
        return sHA256


    # Temporary: for now generates random id
    # TODO: This can be fixed now
    def generateBlockID(self):

        return 1


    # Temporary: for now generates a random string representation of the signed SHA256
    def generateSignedSHA256(self):

        signedSHA256 = "LKEFALEKFALEK"
        return signedSHA256


    # Setters
    def setFirstName(self, fName):

        self._firstName = fName


    def setLastName(self, lName):

        self._lastName = lName


    def setSSN(self, ssn):

        self._SSN = ssn


    def setSignedSHA256(self, signedSHA):

        self._signedSHA256 = signedSHA


    def setBlockId(self, bID):

        self._blockID = bID


    def setVerificationProcessID(self, vpID):

        self._verificationProcessID = vpID


    def setSHA256String(self, shaString):

        self._SHA256String = shaString


    # TODO: check how process Id is selected and used
    def generateProcessId(self):
        return 2


    # TODO: Add more attributes to return
    def toString(self):
        return "Name: " + self._firstName + " " + self._lastName + " Provider: " + self._provider + " Time: " + self._timestamp


    #Getters
    def getSSN(self):

        return self._SSN


    def getSignedSHA256(self):

        return self._signedSHA256


    def getBlockId(self):

        return self._blockID


    def getVerificationProcessID(self):

        return self._verificationProcessID


    def getSHA256String(self):

        return self._SHA256String


    def getNext(self):

        return self._next


    def getFirstName(self):

        return self._firstName


    def getLastName(self):

        return self._lastName


    def getProvider(self):

        return self._provider


    def getTimestamp(self):

        return self._timestamp


    def setTimestamp(self, ts):

        self._timestamp = ts