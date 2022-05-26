from course import *
from courselist import *
import re

course_list = CourseList()

with open("data.txt", "r") as data_file:
    for line in data_file:
        line = line.strip()
        re.split('[,]', line)
        line = line.split(',')
        num = line[0]
        name = line[1]
        credit = line[2]
        grade = line[3]
        new_course = Course(num, name, credit, grade)
        this_node = Node(new_course)
        course_list.insert(this_node)
    data_file.close()

course_list.__str__()

print(course_list.is_sorted())

course_list.insertion_sort_singly_linked()
print()
course_list.__str__()

print(f"Size of list is {course_list.list_size()}")


course_list.remove(2420)
course_list.__str__()
print(f"Size of list is {course_list.list_size()}")

print()
print()

# course_list.remove_all()
# course_list.__str__()
# print(f"Size of list is {course_list.list_size()}")

print()
print()
course_list.calculate_gpa()
print()
print()


print(course_list.is_sorted())


#this_course = course_list.find(2810)

# print(this_course.__str__())
# print(this_course.name())

