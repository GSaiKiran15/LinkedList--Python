from linkedlist import Node, LinkedList


def merged_lists(first_list, second_list, merged_list):
    current_first = first_list.head
    current_second = second_list.head
    while True:
        if current_first is None:
            merged_list.insert_end(current_second)
            break
        elif current_second is None:
            merged_list.insert_end(current_first)
            break
        elif current_first.data < current_second.data:
            current_first_next = current_first.next
            current_first.next = None
            merged_list.insert_end(current_first)
            current_first = current_first_next
        elif current_first.data > current_second.data:
            current_second_next = current_second.next
            current_second.next = None
            merged_list.insert_end(current_second)
            current_second = current_second_next


print("Printing First List\n")

first_list = LinkedList()
node1 = Node("1")
node2 = Node("3")
node3 = Node("4")
first_list.insert_end(node1)
first_list.insert_end(node2)
first_list.insert_end(node3)
first_list.print_list()

print("\nPrinting Second List\n")

second_list = LinkedList()
node4 = Node("2")
node5 = Node("7")
node6 = Node("9")
second_list.insert_end(node4)
second_list.insert_end(node5)
second_list.insert_end(node6)
second_list.print_list()

merged_list = LinkedList()
print("\nPrinting Merged lists\n")
merged_lists(first_list, second_list, merged_list)
merged_list.print_list()


