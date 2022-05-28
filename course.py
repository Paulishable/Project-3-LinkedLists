"""this module contains the class for a course"""


class Course:
    """this class contains the info for a course"""

    def __init__(self, a_number=0, a_name="", a_credits=0.0, a_grade=0.0):
        try:
            isinstance(a_number, int)
            isinstance(a_name, str)
            isinstance(a_credits, float)
            isinstance(a_grade, float)
        except ValueError:
            raise ValueError("ValueError exception thrown")

        if a_name is None or int(a_number) < 0 or float(a_credits) < 0.0 or float(a_grade) < 0.0:
            raise ValueError("ValueError exception thrown")

        self.the_number = 0
        self.the_name = ""
        self.the_credits = 0.0
        self.the_grade = 0.0
        self.next = None
        self.data = self
        self.the_number = a_number
        self.the_name = a_name
        self.the_credits = a_credits
        self.the_grade = a_grade


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

    def get_data(self):
        """this is the grade received for the course"""
        return self

    def get_next(self):
        """this is the grade received for the course"""
        return self.next

    def set_next(self, next_name):
        """this is the grade received for the course"""
        self.next = next_name

    def __str__(self):
        return f"{self.the_number} {self.the_name} Grade:{self.the_grade} Credit Hours:" \
               f" {float(self.the_credits)}"
