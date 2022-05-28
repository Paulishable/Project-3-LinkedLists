'''This is the main program for Project 3'''
import re
from courselist import CourseList, Node
from course import Course


course_list = CourseList()

with open("data.txt", "r", encoding="utf-8") as data_file:
    for line in data_file:
        line = line.strip()
        re.split('[,]', line)
        line = line.split(',')
        num = line[0]
        name = line[1]
        credit = line[2]
        grade = line[3]
        new_course = Course(int(num), name, float(credit), float(grade))
        this_node = Node(new_course)
        course_list.insert(this_node)

    data_file.close()
