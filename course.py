"""this module contains the class for a course"""
class Course:
    """this class contains the info for a course"""
    def __init__(self, the_number=0, the_name="", the_credits=0.0, the_grade=0.0):
        self.the_number = the_number
        self.the_name = the_name
        self.the_credits = the_credits
        self.the_grade = the_grade

    def number(self):
        """this is the course number"""
        return self.the_number

    def name(self):
        """this is the course name"""
        return self.the_name

    def credit_hr(self):
        """this is the credits given for the course"""
        return self.the_credits

    def grade(self):
        """this is the grade received for the course"""
        return self.the_grade

    def __str__(self):
        return f"{self.the_number} {self.the_name} Grade:{self.the_grade} Credit Hours:" \
               f" {float(self.the_credits)}"
