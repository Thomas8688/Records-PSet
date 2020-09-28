#THIS PORTION OF CODE ADJUSTED FROM THE INTERNET
import datetime
import calendar
#-

class Record:
    def __init__(self, forename, surname, dob, gender,  csStudent):
        if not isinstance(forename, str):
            raise TypeError("Forename must be a String")
        else:
            self.__forename = forename
        if not isinstance(surname, str):
            raise TypeError("Surname must be a String")
        else:
            self.__surname = surname

        if not isinstance(dob, str):
            raise TypeError("Date of Birth must be a String")
        else:
            if dob[4] == "-" and dob[7] == "-":
                try:
                    int(dob[0])
                    int(dob[1])
                    int(dob[2])
                    int(dob[3])
                    int(dob[5])
                    int(dob[6])
                    int(dob[8])
                    int(dob[9])
                    self.__dob = dob
                except:
                    raise ValueError("Date of Birth must be in the form (xxxx-xx-xx)")
            else:
                raise ValueError("Date of Birth must be in the form (xxxx-xx-xx)")

        if gender.upper() not in ["M", "F", "O"]:
            raise ValueError("Gender must be in (M, F, O)")
        else:
            self.__gender = gender.upper()
        if not isinstance(csStudent, bool):
            raise TypeError("csStudent must be Boolean")
        else:
            self.__csStudent = csStudent
#- THIS PORTION OF CODE ADJUSTED FROM THE INTERNET
        self.__created = datetime.datetime.now()
#-

    def setForename(self, forename):
        if not isinstance(forename, str):
            raise TypeError("Forename must be a String")
        else:
            self.__forename = forename

    def setSurname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Surname must be a String")
        else:
            self.__surname = surname

    def setGender(self, gender):
        if gender.upper() not in ["M", "F", "O"]:
            raise ValueError("Gender must be in [M, F, O]")
        else:
            self.__gender = gender.upper()

    def setcsStudent(self, csStudent):
        if not isinstance(csStudent, bool):
            raise TypeError("csStudent must be Boolean")
        else:
            self.__csStudent = csStudent

    def getForename(self):
        print("\n"+self.__forename)

    def getSurname(self):
        print("\n"+self.__surname)

    def getDob(self):
        print("\n"+self.__dob)

    def getAge(self):
        dob = self.__dob
#-THIS PORTION OF CODE ADJUSTED FROM THE INTERNET
        today = datetime.date.today().isoformat()
#-
        today = today.split("-")
        dob = dob.split("-")
        curyear = int(today[0])
        biryear = int(dob[0])
        age = (curyear - biryear)
        if today[1] == dob[1]:
            if today[2] < dob[2]:
                age -= 1
        elif today[1] < dob[1]:
            age -= 1
        print(age)

    def getGender(self):
        print("\n"+self.__gender)

    def getCsStudent(self):
        print("\n"+self.__csStudent)

    def getCreated(self):
        print("\n"+str(self.__created))

    def getCreateddate(self):
        print("\n"+str(self.__createddate))

    def day_born(self):
        dob = self.__dob
        dob = dob.split("-")
#THIS PORTION OF CODE ADJUSTED FROM THE INTERNET
        dob = dob[2]+' '+dob[1]+' '+dob[0]
        dob = datetime.datetime.strptime(dob, '%d %m %Y').weekday()
        print(calendar.day_name[dob])
#-


    def printValues(self):
        print("\n")
        print(self.__forename)
        print(self.__surname)
        print(self.__dob)
        self.getAge()
        print(self.__gender)
        print(self.__csStudent)





student1 = Record("Tom", "Eley", "2004-09-15", "M", True)
student1.printValues()
student1.day_born()
