"""This is the ClassList and Node file"""


class Node():
    """Node class fpr linked list class"""
    def __init__(self, data_for_this_node, next_stuff=None):
        self.data = data_for_this_node
        self.next = next_stuff

    def get_next(self):
        """next node"""
        return self.next

    def set_next(self, next_item):
        """set the next item"""
        self.next = next_item

    def get_data(self):
        """get the data"""
        return self.data

    def set_data(self, data_item):
        """set the data item"""
        self.data = data_item


class CourseList():
    """this is the Class for the linked list"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = self.head

    def insert(self, new_node):
        """insert and sort an element into the link list = a course"""
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.insertion_sort_singly_linked()

    def size(self):
        """calculate the length of the linked list"""
        count = 0
        current_node = self.head  # Start at head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def insertion_sort_singly_linked(self):
        """insertion sort for singly linked lists"""
        before_current = self.head
        current_node = self.head.next
        while current_node is not None:
            next_node = current_node.next
            position = self.find_insertion_position(current_node.data.number())
            if position == before_current:
                before_current = current_node
            else:
                self.remove_after(before_current)
                if position is None:
                    self.prepend(current_node)
                else:
                    self.insert_after(position, current_node)
            current_node = next_node

    def find_insertion_position(self, data_value):
        """resource function for insertion sort"""
        position_a = None
        position_b = self.head
        while (position_b is not None) and (data_value > position_b.data.number()):
            position_a = position_b
            position_b = position_b.next
        return position_a

    def remove(self, this_course_number):
        """removes a course from the list by course number"""
        this_node = self.head
        prev_node = None

        while this_node:
            if str(this_node.get_data().number()) == str(this_course_number):
                if prev_node:
                    prev_node.set_next(this_node.next)
                else:
                    self.head = this_node.next
                return True  # data removed
            prev_node = this_node
            this_node = this_node.next
        return False  # data not found

    def remove_all(self, course_number):
        """Remove all instances of the course number"""
        curr_node = self.head
        while curr_node is not None:
            if str(curr_node.data.number()) == str(course_number):
                self.remove(curr_node.data.number())
            curr_node = curr_node.next

    def find(self, course_number):
        """find the course given the course number"""
        this_node = self.head
        while this_node is not None:
            if str(this_node.get_data().number()) == str(course_number):
                return this_node.get_data()
            this_node = this_node.next
        return -1

    def prepend(self, new_node):
        """put a new_node in the head of the list"""
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        """put a node after thr current node"""
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_after(self, current_node):
        """remove the node after the current node"""
        # Special case, remove head
        if (current_node is None) and (self.head is not None):
            succeeding_node = self.head.next
            self.head = succeeding_node
            if succeeding_node is None:  # Remove last item
                self.tail = None
        elif current_node.next is not None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node is None:  # Remove tail
                self.tail = current_node

    def search_my_courses(self, key):
        """search courses by ket which is not defined yet (it should be an attribute of course)"""
        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                return current_node
            current_node = current_node.next
        return None

    def __str__(self):
        current_node = self.head  # Start at head
        while current_node is not None:
            print(current_node.get_data().__str__())
            current_node = current_node.next
        return "Done"

    def calculate_gpa(self):
        """calculate the cumulate GPA of all the courses"""
        current_node = self.head  # Start at head
        total_credit_hrs = float(0.0)
        total_grade_points = float(0.0)
        final_gpa = 0.0
        while current_node is not None:
            total_credit_hrs += float(current_node.get_data().credit_hr())
            total_grade_points += float(current_node.get_data().credit_hr()) * \
                                  float(current_node.get_data().grade())
            final_gpa = total_grade_points / total_credit_hrs
            current_node = current_node.next
        print(f"Cumulative GPA:  {final_gpa}")
        return final_gpa

    def is_sorted(self):
        """determine if the linked list is sorted or not"""
        current_node = self.head  # Start at head
        while current_node is not None:
            course_number_last = current_node.get_data().number()
            current_node = current_node.next
            if current_node is not None:
                course_number_next = current_node.get_data().number()
                if course_number_next < course_number_last:
                    return False
        return True

    def add(self, a_course):
        """add a course"""
        new_node = Node(a_course, self.head)
        self.head = new_node
        #self.size += 1

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        item = self.current.data
        self.current = self.current.next
        return item

    # def insert(self, new_node):
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     elif self.tail is not None:
    #         if new_node.get_data().number() < self.tail.get_data().number():
    #             self.prepend(new_node)
    #         else:
    #             self.tail.next = new_node
    #             self.tail = new_node
