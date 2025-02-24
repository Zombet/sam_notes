class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def insert_front(head):
    data = int(input("Enter data to insert at the front: "))
    new_node = Node(data)
    new_node.link = head
    return new_node


def insert_rear(head):
    data = int(input("Enter data to insert at the rear: "))
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.link:
        current = current.link
    current.link = new_node
    return head


def delete_front(head):
    if head is None:
        print("Linked List is empty. Nothing to delete.")
        return None
    print(f"Element deleted from front: {head.data}")
    return head.link


def delete_end(head):
    if head is None:
        print("Linked List is empty. Nothing to delete.")
        return None

    if head.link is None:
        print(f"Element deleted from end: {head.data}")
        return None

    current = head
    while current.link.link:
        current = current.link
    print(f"Element deleted from end: {current.link.data}")
    current.link = None
    return head


def insert_at_pos(head):
    pos = int(input("Enter the position to insert: "))
    if pos < 1:
        print("Invalid position. Position must be >= 1.")
        return head

    cnt = 0
    temp = head
    while temp:
        cnt += 1
        temp = temp.link

    if pos > cnt + 1:
        print(f"Invalid position. The list has only {cnt} elements.")
        return head

    if pos == 1:
        return insert_front(head)
    elif pos == cnt + 1:
        return insert_rear(head)

    data = int(input("Enter data to insert: "))
    new_node = Node(data)

    current = head
    for _ in range(pos - 2):
        current = current.link

    new_node.link = current.link
    current.link = new_node
    return head


def delete_at_pos(head):
    if head is None:
        print("Linked List is empty. Nothing to delete.")
        return head

    cnt = 0
    temp = head
    while temp:
        cnt += 1
        temp = temp.link

    pos = int(input("Enter the position to delete: "))
    if pos < 1 or pos > cnt:
        print(f"Invalid position. The list has only {cnt} elements.")
        return head

    if pos == 1:
        return delete_front(head)

    current = head
    for _ in range(pos - 2):
        current = current.link

    to_delete = current.link
    current.link = to_delete.link
    print(f"Element deleted from position {pos}: {to_delete.data}")
    return head


def display(head):
    if head is None:
        print("Linked List is empty.")
        return

    print("Linked List Contents:")
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.link
    print("None")


def display_reverse(head):
    if head is None:
        return
    display_reverse(head.link)
    print(head.data, end=" -> ")


def menu():
    head = None

    while True:
        print("\n--- Linked List Operations ---")
        print("1. Insert at Front")
        print("2. Insert at Rear")
        print("3. Insert at Position")
        print("4. Delete at Front")
        print("5. Delete at Rear")
        print("6. Delete at Position")
        print("7. Display Linked List")
        print("8. Display Linked List in Reverse")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            head = insert_front(head)
        elif choice == 2:
            head = insert_rear(head)
        elif choice == 3:
            head = insert_at_pos(head)
        elif choice == 4:
            head = delete_front(head)
        elif choice == 5:
            head = delete_end(head)
        elif choice == 6:
            head = delete_at_pos(head)
        elif choice == 7:
            display(head)
        elif choice == 8:
            print("Linked List in Reverse:")
            display_reverse(head)
            print("None")
        elif choice == 9:
            print("Exiting the program. Thanks for using Linked List!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()