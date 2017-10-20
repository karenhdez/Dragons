


class Person:

    def __init__(self, f, l, ssn, dob):

        self.__firstName = f
        self.__lastName = l
        self.__birthDate = dob
        self.__ssn = ssn


    # TODO: Add more attributes to return
    def toString(self):

        return "Name: " + self.firstName + " " + self.lastName + " Provider: " + self.provider + " Time: " + self.timestamp


    @property
    def firstName(self):
        return self.__firstName

    def lastName(self):
        return self.__lastName

    def birthDate(self):
        return self.__birthDate

    def ssn(self):
        return self.__ssn


    # Setters
    @firstName.setter
    def firstName(self, val):
        pass

    @lastName.setter
    def lastName(self, val):
        pass

    @birthDate.setter
    def birthDate(self, val):
        pass

    @ssn.setter
    def ssn(self, val):
        pass