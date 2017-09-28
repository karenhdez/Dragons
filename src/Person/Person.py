


class Person:

    def __init__(self, f, l, ssn, dob):

        self.firstName = f
        self.lastName = l
        self.birthDate = dob
        self.ssn = ssn


    # TODO: Add more attributes to return
    def toString(self):

        return "Name: " + self.firstName + " " + self.lastName + " Provider: " + self.provider + " Time: " + self.timestamp


    # Setters
    def setFirstName(self, fName):

        self.firstName = fName


    def setLastName(self, lName):

        self.lastName = lName


    def setSSN(self, ssn):

        self.ssn = ssn


    # Getters
    def getFirstName(self):

        return self.firstName


    def getLastName(self):

        return self.lastName


    def getSSN(self):

        return self.ssn