from Record import *
import hashlib
import rsa


class Block(object):

    def __init__(self, data, next):

        self.__data = data
        self.__next = next

        self.__blockID = self.generateBlockID()
        self.__SHA256 = self.generateSHA256()

        #verification
        self.__processID = self.generateProcessId()

        self.__signedSHA256 = ""
        self.__timestamp = ""

        self.__pubkey = ""
        self.__privkey = ""

        self.__verified = False


    # Getters
    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @property
    def blockID(self):
        return self.__blockID

    @property
    def SHA256(self):
        return self.__SHA256

    @property
    def processID(self):
        return self.__processID

    @property
    def signedSHA256(self):
        return self.__signedSHA256

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def pubkey(self):
        return self.__pubkey

    @property
    def privkey(self):
        return self.__privkey

    @property
    def verified(self):
        return self.__verified


    # Setters
    @data.setter
    def data(self, val):
        pass

    @next.setter
    def next(self, val):
        pass

    @blockID.setter
    def blockID(self, val):
        pass

    @SHA256.setter
    def SHA256(self, val):
        pass

    @processID.setter
    def processID(self, val):
        pass

    @signedSHA256.setter
    def signedSHA256(self, val):
        pass

    @timestamp.setter
    def timestamp(self, val):
        pass

    @pubkey.setter
    def pubkey(self, val):
        pass

    @privkey.setter
    def privkey(self, val):
        pass

    @verified.setter
    def verified(self, val):
        pass


    def generateSHA256(self, h_last):

        s = h_last + self.data.toString()
        h_full = hashlib.sha256(s).hexdigest()

        return h_full


    def generateBlockID(self):

        return 0


    def signSHA256(self):

        hash = self.SHA256.encode('utf8')

        (self.pubkey, self.privkey) = rsa.newkeys(512)
        signedSHA = rsa.encrypt(hash, self.pubkey)

        self.signedSHA256 = signedSHA


    def generateProcessId(self):

        return 0