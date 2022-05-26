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

# course_list.__str__()

# print(course_list.is_sorted())
#
# course_list.insertion_sort_singly_linked()
# print()
course_list.__str__()
course_list.calculate_gpa()
#
# print(f"Size of list is {course_list.list_size()}")
#
#
#
#
#
#
# #course_list.remove(2420)
# course_list.__str__()
print(f"Size of list is {course_list.size()}")
#
# print()
# print()
#
# # course_list.remove_all()
# # course_list.__str__()
# # print(f"Size of list is {course_list.list_size()}")
#
# print()
# print()
# print()
# print()
#
#
# print(course_list.is_sorted())
#
#
# #this_course = course_list.find(2810)
#
# # print(this_course.__str__())
# # print(this_course.name())
# print()
# print()
# print()
# print()
# print()
# print()
#
#
iter_list = course_list.__iter__()

try:
    print(iter_list.__next__())
    print(iter_list.__next__())
    print(iter_list.__next__())
    print(iter_list.__next__())
    print(iter_list.__next__())
except:
    print("out of items")


# test_course_creation()
# test_course_creation_with_parameters()
# test_empty_courselist()
# test_insert()
# test_remove()
# test_remove_all()
# test_gpa()
# test_iterate_list()
# test_code_quality()
