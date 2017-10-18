from .Person import *


class Patient(Person):

    def __init__(self, f, l, ssn, dob, doc, p):

        super(self.__class__, self).__init__(f, l, ssn, dob)

        self.doctor = doc
        self.provider = p


    def setDoctor(self, d):

        self.doctor = d


    def getDoctor(self):

        return self.doctor


    def setProvider(self, p):

        self.provider = p


    def getProvider(self):

        return self.provider