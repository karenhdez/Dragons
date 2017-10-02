import datetime


class Record(object):

    def __init__(self, f, l, ssn, p):

        self.__firstName = f
        self.__lastName = l
        self.__SSN = ssn
        self.__provider = p
        self.__timestamp = str(datetime.datetime.now()).split('.')[0]


    # Getters
    @property
    def firstName(self):
        return self.__firstName

    @property
    def lastName(self):
        return self.__lastName

    @property
    def SSN(self):
        return self.__SSN

    @property
    def provider(self):
        return self.__provider

    @property
    def timestamp(self):
        return self.__timestamp

    # Setters
    @firstName.setter
    def firstName(self, val):
        pass

    @lastName.setter
    def lastName(self, val):
        pass

    @SSN.setter
    def SSN(self, val):
        pass

    @provider.setter
    def provider(self, val):
        pass

    @timestamp.setter
    def timestamp(self, val):
        pass


    # TODO: Add more attributes to return
    def toString(self):

        return self.__firstName + self.__lastName + str(self.__SSN) + self.__provider + self.__timestamp