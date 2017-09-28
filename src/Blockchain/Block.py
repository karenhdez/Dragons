from Record import *


class Block:

    def __init__(self):

        self.data = None
        self.blockID = self.generateBlockID()
        self.SHA256 = self.generateSHA256()
        self.verified = False


    # Temporary: for now generates random string
    def generateSHA256(self):

        sHA256 = "WELKFRLEA"
        return sHA256


    # Temporary: for now generates random id
    # TODO: This can be fixed now
    def generateBlockID(self):

        return 1



class VerifiedBlock(Block):

    def __init__(self):

        super(self.__class__, self).__init__()

        self.blockID = None
        self.processID = self.generateProcessId()
        self.signedSHA256 = ""
        self.timestamp = None
        self.verified = True


    def setSignedSHA256(self, signedSHA):

        self._signedSHA256 = signedSHA


    def setBlockId(self, bID):

        self.blockID = bID


    def setVerificationProcessID(self, vpID):

        self.verificationProcessID = vpID


    def setSHA256String(self, shaString):

        self.SHA256String = shaString


    # Temporary: for now generates a random string representation of the signed SHA256
    def generateSignedSHA256(self):

        signedSHA256 = "LKEFALEKFALEK"
        return signedSHA256


    # TODO: check how process Id is selected and used
    def generateProcessId(self):

        return 2


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



class UnverifiedBlock(Block):

    def __init__(self):

        super(self.__class__, self).__init__()

        self.verified = False