# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   Olivier Richer,6/6/2025,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# TODO Create a Person Class
# TODO Add first_name and last_name properties to the constructor
# TODO Create a getter and setter for the first_name property
# TODO Create a getter and setter for the last_name property
# TODO Override the __str__() method to return Person data
class Person:
    """
    A class representing person data.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.


    ChangeLog: (Who, When, What)
    O.Richer, 6/06/2025,Created Class
    """
# constructor. so what is that? In a nutshell it is a way to create objects with some initial set of values
# initially my person has no first_name, no Last_name. and with the idea of Constructor we can pass those in
# as an argument to our object itself. so init for "initialization".
    def __init__(self,first_name: str="", last_name: str=""):
      self.first_name = first_name
      self.last_name = last_name

#Properties are a way to get and set instances variables and allow us to put an extra type checking or data validation
# or just extra logic whenever a class is trying to access instances variables.
# ._ is a "notation" perhaps we should call it a "code" that tells python, there are meant to be secret variables and
#( in a perfect world) no one outside of this class is supposed to get access to them.
    @property
    def first_name(self):
      return self.__first_name.title()
# The extra benefits of properties is that you can also put data validation on this. that means that whenever someone
#tries to set a value here it is going to call this method instead (  .setter)

    @first_name.setter
    def first_name(self, value: str):
     if value.isalpha() or value == "":
        self.__first_name = value
     else:
        raise ValueError("First name can only have alphabetic character .")
# the last_name deal is the same as above. Just a repeat.
    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value =="" :
            self.__last_name = value
        else:
            raise ValueError("Last name can only have alphabetic character ")
# The "__str__" method return a string representation of an object. here the first name, and the last name of a person.
# In other words, the string method converts the data inside our data class ( student) into a string.
    def __str__(self):
        return f"{self.first_name},{self.last_name}"

# TODO Create a Student class the inherits from the Person class
# TODO call to the Person constructor and pass it the first_name and last_name data
# TODO add a assignment to the course_name property using the course_name parameter
# TODO add the getter for course_name
# TODO add the setter for course_name
# TODO Override the __str__() method to return the Student data
# Inheritance! what is it? while one could probably take the work of this prolific french writer from the 19th century
# in which Balzac wrote about the growing wealth divide in europe in the 19th century and still is to this time and
# explain the idea.
# we will stay in the computer science sphere.
# Inheritance  is this idea that a class can be extended upon to have multiple implementations.
# Inheritance allows us to create a base class ( something generic). In our case the class Person, and it allows us to
#uniquely extend that class to add additional information. In our case, the additional information will be the class
# taken by the student.
# in brief, the class student is going to inherit  everything that comes from the class person ( first name,last name)
# and so in order to use that "inheritance" properly. One still need to go back to that idea on constructor.
# Meaning one needs to find a way to initialize the information properly.
# well, we will call " super constructor".

class Student(Person):
    """

    class student inherit from the class person , class student represent a student data
    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        course_name (str): The course taken by the student.

    ChangeLog: (Who, When, What)
    O.Richer, 6/06/2025,Created Class

    """
    def __init__(self,first_name: str = "",last_name: str = "",course_name: str = ""):
        super().__init__(first_name = first_name, last_name = last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        return self.__course_name.title()

    @course_name.setter
    def course_name(self, value: str):
        if value:
            self.__course_name = value
        else:
            raise ValueError("please enter Course name .")
# Override the Person __str__() method behavior to return a coma-separated string of data
    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.course_name}"


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    Change Log:
    RRoot, 1.1.2030, Created class
    """


    @staticmethod
    def read_data_from_file(file_name: str, student_objects :list):
            #student_objects = []
            #file = None
            try:
                file = open(file_name, "r")
                json_students = json.load(file)
                # to convert dictionary data to Student data
                for student in json_students:
                    student_object = Student(first_name=student["FirstName"],
                                              last_name=student["LastName"],
                                              course_name=student["CourseName"])
                    student_objects.append(student_object)
            except FileNotFoundError as e:
                IO.output_error_messages( "Text file must exist before running this script!")
            except Exception as e:
                IO.output_error_messages("Error: there was a problem with reading file.", e)
            finally:
                if file and not file.closed:
                    file.close()
            return student_objects





    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):

     """
     This function writes data to a json file with data from
        a list of dictionary rows

        Change Log:
        RRoot, 1.1.2030, Created function
        """
     try:
         student_data_dictionary: list = []
         for student in student_data:
             student_json: dict = {
                 "FirstName": student.first_name,
                 "LastName": student.last_name,
                 "CourseName": student.course_name
             }
             student_data_dictionary.append(student_json)

         file = open(file_name, 'w')
         json.dump(student_data_dictionary, file, indent=2)
         file.close()
         print()
         print("Here is the data you just saved!:")
         IO.output_student_and_course_names(student_data=student_data)
     except Exception as e:
         message = "Error: There was a problem with writing to the file.\n"
         message += "Please check that the file is not open by another program."
         IO.output_error_messages(message=message, error=e)
     finally:
         if not file.closed:
             file.close()





# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    Change Log:
    RRoot, 1.1.2030, Created class
    RRoot, 1.2.2030, Added menu output and input functions
    RRoot, 1.3.2030, Added a function to display the data
    RRoot, 1.4.2030, Added a function to display custom error messages
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):

        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():

        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):

        print("-" * 50)
        for student in student_data:
            print (student)


        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):


        try:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            course_name = input("Enter course name: ")
            student = Student( first_name=first_name,last_name=last_name,course_name=course_name)




            student_data.append(student)
            print()
            print(f"You have Registered {first_name} {last_name} for {course_name}")
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data! ", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)
        return student_data









# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_objects = students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3 or 4")

print("Program Ended")


