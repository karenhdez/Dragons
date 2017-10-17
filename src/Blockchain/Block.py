from Record import *
import hashlib
import rsa
import jwt


class Block(object):

    def __init__(self, data):

        self.__data = data

        self.__blockID = self.generateBlockID()
        self.__SHA256 = self.generateSHA256()


    # Getters
    @property
    def data(self):
        return self.__data

    @property
    def blockID(self):
        return self.__blockID

    @property
    def SHA256(self):
        return self.__SHA256


    # Setters
    @data.setter
    def data(self, val):
        pass

    @blockID.setter
    def blockID(self, val):
        pass

    @SHA256.setter
    def SHA256(self, val):
        pass


    def generateSHA256(self, h_last):

        s = h_last + self.__data.toString()
        h_full = hashlib.sha256(s).hexdigest()

        return h_full


    def generateBlockID(self):

        return 0



class UnverifiedBlock(object):

    def __init__(self, data):

        self.__verified = False


    @property
    def verified(self):
        return self.__verified

    @verified.setter
    def verified(self, val):
        pass



class VerifiedBlock(Block):

    def __init__(self, data):

        super(self.__class__, self).__init__(data)

        self.__processID = self.generateProcessId()

        self.__signedSHA256 = ""
        self.__timestamp = ""

        self.__pubkey = ""
        self.__privkey = ""

        self.__verified = True


    # Getters
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


    def encodeJWT(self, s):

        jwt.encode()
        return jwt.encode(s, 'secret', algorithm='HS256')


    def signSHA256(self, pubkey):

        hash = self.__SHA256.encode('utf8')

        #(self.__pubkey, self.__privkey) = rsa.newkeys(512)
        signedSHA = rsa.encrypt(hash, pubkey)

        self.__signedSHA256 = signedSHA


    def generateProcessId(self):

        return 0