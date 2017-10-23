from .Person import *


class Patient(Person):

    def __init__(self, f, l, ssn, dob, doc, p):

        super(self.__class__, self).__init__(f, l, ssn, dob)

        self.__doctor = doc
        self.__provider = p


    @property
    def doctor(self):
        return self.__doctor

    @property
    def provider(self):
        return self.__provider

    # Setters
    @doctor.setter
    def doctor(self, val):
        pass

    @provider.setter
    def provider(self, val):
        pass