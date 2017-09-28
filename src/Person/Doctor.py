from Person import *


class Doctor(Person):

    def __init__(self, f, l, ssn, dob, s):

        super(self.__class__, self).__init__(f, l, ssn, dob)

        self.specialty = s


    def setSpecialty(self, s):

        self.specialty = s


    def getSpecialty(self):

        return self.specialty