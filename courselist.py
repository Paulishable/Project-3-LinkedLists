class Node(object):

    def __init__(self, d, n=None):
        self.data = d
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class CourseList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def list_size(self):
        count = 0
        curNode = self.head  # Start at head
        while curNode is not None:
            count += 1
            curNode = curNode.next
        return count

    def insertion_sort_singly_linked(self):
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
        position_a = None
        position_b = self.head
        while (position_b is not None) and (data_value > position_b.data.number()):
            position_a = position_b
            position_b = position_b.next
        return position_a

    def remove(self, d):
        this_node = self.head
        prev_node = None

        while this_node:
            if str(this_node.get_data().number()) == str(d):
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head = this_node.get_next()
                return True  # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def remove_all(self):
        curNode = self.head  # Start at head
        while curNode is not None:
            self.remove(curNode.get_data().number())
            curNode = curNode.next

    def find(self, d):
        this_node = self.head
        while this_node is not None:
            if str(this_node.get_data().number()) == str(d):
                return this_node.get_data()
            else:
                this_node = this_node.get_next()
        return -1

    def prepend(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
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
        current_node = list.head
        while current_node is not None:
            if current_node.data == key:
                return current_node
            current_node = current_node.next
        return None

    def __str__(self):
        curNode = self.head  # Start at head
        while curNode is not None:
            print(curNode.get_data().__str__())
            curNode = curNode.next

    def calculate_gpa(self):
        curNode = self.head  # Start at head
        total_credit_hrs = float(0.0)
        total_grade_points = float(0.0)
        while curNode is not None:
            total_credit_hrs += float(curNode.get_data().credit_hr())
            total_grade_points += float(curNode.get_data().credit_hr()) * float(curNode.get_data().grade())
            final_gpa = total_grade_points / total_credit_hrs
            curNode = curNode.next
        print(f"Cumulative GPA: ",  "%.3f" % (final_gpa))
        return final_gpa

    def is_sorted(self):
        curNode = self.head  # Start at head
        while curNode is not None:
            course_number_last = curNode.get_data().number()
            curNode = curNode.next
            if curNode is not None:
                course_number_next = curNode.get_data().number()
                if course_number_next < course_number_last:
                    return False
        return True


    def add(self, d):
        new_node = Node(d, self.head)
        self.head = new_node
        self.size += 1
