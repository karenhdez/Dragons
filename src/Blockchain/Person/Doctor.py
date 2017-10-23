from .Person import *


class Doctor(Person):

    def __init__(self, f, l, ssn, dob, s):

        super(self.__class__, self).__init__(f, l, ssn, dob)

        self.__specialty = s


    @property
    def specialty(self):
        return self.__specialty

    # Setters
    @specialty.setter
    def specialty(self, val):
        pass