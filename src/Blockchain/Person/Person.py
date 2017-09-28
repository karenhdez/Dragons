


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



class Doctor(Person):

    def __init__(self, f, l, ssn, dob, s):

        super(self.__class__, self).__init__(f, l, ssn, dob)

        self.specialty = s


    def setSpecialty(self, s):

        self.specialty = s


    def getSpecialty(self):

        return self.specialty