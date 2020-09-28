class Record:
    def __init__(self):
        self.__forename = None
        self.__surname = None
        self.__age = None
        self.__gender = None
        self.__CsStudent = None
        self.setValues()

    def setValues(self):
        self.setForename()
        self.setSurname()
        self.setAge()
        self.setGender()
        self.setCsStudent()

    def setForename(self):
        forename = input("Forename: ")
        self.__forename = forename

    def setSurname(self):
        surname = input("Surname: ")
        self.__surname = surname

    def setAge(self):
        quit = False
        while not quit:
            age = input("Age: ")
            try:
                age = int(age)
                self.__age = age
                quit = True
            except:
                print("Invalid Age")

    def setGender(self):
        quit = False
        validinput = ["m", "f", "o"]
        while not quit:
            gender = input("Gender(M,F,O): ")
            if gender.lower() in validinput:
                self.__gender = gender.upper()
                quit = True
            else:
                print ("Invalid Gender")

    def setCsStudent(self):
        quit = False
        validinput = ["true", "false", True, False]
        while not quit:
            CsStudent = input("CS Student(True, False): ")
            if CsStudent.lower() in validinput:
                if CsStudent.lower() == "false":
                    self.__CsStudent = False
                else:
                    self.__CsStudent = True
                quit = True
            else:
                print("Invalid Response")

    def getForename(self):
        print("\n"+self.__forename)

    def getSurname(self):
        print("\n"+self.__surname)

    def getAge(self):
        print("\n"+str(self.__age))

    def getGender(self):
        print("\n"+self.__gender)

    def getCsStudent(self):
        print("\n"+self.__CsStudent)
        
    def printValues(self):
        print("\n")
        print(self.__forename)
        print(self.__surname)
        print(self.__age)
        print(self.__gender)
        print(self.__CsStudent)

student1 = Record()
student1.printValues()
