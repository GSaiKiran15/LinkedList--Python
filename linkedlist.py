# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_list_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def list_length(self):
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    def insert_head(self, new_node):
        temp = self.head
        self.head = new_node
        self.head.next = temp
        del temp

    def insert_at(self, new_node, position):
        if position < 0 or position > linked_list.list_length():
            print("Invalid length")
            return
        if position == 0:
            self.insert_head(new_node)
            return
        current_node = self.head
        current_position = 0
        while True:
            if current_position == position:
                previous_node.next = new_node
                new_node.next = current_node
                break
            previous_node = current_node
            current_node = current_node.next
            current_position += 1

    def insert_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node

    def delete_head(self):
        if self.is_list_empty() is False:
            previous_head = self.head
            self.head = self.head.next
            previous_head.next = None
        else:
            print("List is empty. Delete FAILED!!")

    def delete_at(self, position):
        if position < 0 or position >= self.list_length():
            print("Invalid Position")
            return
        if self.is_list_empty() is False:
            if position == 0:
                self.delete_head()
                return
            current_node = self.head
            current_position = 0
            while True:
                if current_position == position:
                    previous_node.next = current_node.next
                    current_node.next = None
                    break
                previous_node = current_node
                current_node = current_node.next
                current_position += 1
        else:
            print("List is empty")

    def delete_end(self):
        if self.is_list_empty() is False:
            if self.head.next is None:
                self.delete_head()
                return
            last_node = self.head
            while last_node.next is not None:
                previous_node = last_node
                last_node = last_node.next
            previous_node.next = None
        else:
            print("linked list is empty. Delete Failed !")

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next


linked_list = LinkedList()
# for i in range(5):
#     node = Node(str(input("")))
#     linked_list.insert_end(node)
# linked_list.print_list()
#
# first_node = Node("Sai")
# linked_list.insert_end(first_node)
# second_node = Node("Kiran")
# linked_list.insert_end(second_node)
# third_node = Node("Coder")
# linked_list.insert_end(third_node)
# linked_list.print_list()
#
# print("Now Head node is changed")
#
# # Inserting Head Node
# Inserting_head_node = Node("changing head node")
# linked_list.insert_head(Inserting_head_node)
# linked_list.print_list()



# first_node = Node("10")
# linked_list.insert_end(first_node)
# second_node = Node("20")
# linked_list.insert_end(second_node)
# third_node = Node("15")
# linked_list.insert_end(third_node)
# linked_list.print_list()
# print("delete End")
# linked_list.delete_at(1)
# linked_list.print_list()
