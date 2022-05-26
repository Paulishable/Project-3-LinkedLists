class Course:
    def __init__(self, the_number=0, the_name="", the_credits=0.0, the_grade=0.0):
        self.the_number = the_number
        self.the_name = the_name
        self.the_credits = the_credits
        self.the_grade = the_grade

    def number(self):
        return self.the_number

    def name(self):
        return self.the_name

    def credit_hr(self):
        return self.the_credits

    def grade(self):
        return self.the_grade

    def __str__(self):
        return f"{self.the_number} {self.the_name} Grade:{self.the_grade} Credit Hours: {float(self.the_credits)}"



