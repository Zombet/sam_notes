class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_length(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

def get_intersection_node(head1, head2):
    # Calculate the lengths of both linked lists
    len1 = get_length(head1)
    len2 = get_length(head2)
    
    # Align the starting points by advancing the pointer of the longer list
    current1 = head1
    current2 = head2
    
    if len1 > len2:
        for _ in range(len1 - len2):
            current1 = current1.next
    elif len2 > len1:
        for _ in range(len2 - len1):
            current2 = current2.next
    
    # Traverse both lists simultaneously and check for intersection
    while current1 and current2:
        if current1 == current2:  # Intersection found
            return current1
        current1 = current1.next
        current2 = current2.next
    
    # No intersection found
    return None

# Helper function to create linked lists for testing
def create_linked_list(arr):
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Example usage
if __name__ == "__main__":
    # List 1: 1 -> 2 -> 3 -> 4 -> 5
    # List 2: 9 -> 8 -> 4 -> 5 (intersection at node 4)
    
    # Creating two lists with an intersection
    l1=list(map(int, input("Enter the data of 1st list: ").split()))
    head1 = create_linked_list(l1)
    intersect_node = Node(4)
    head1.next.next.next = intersect_node
    head1.next.next.next.next = Node(5)
    l2=list(map(int, input("Enter the data of 2nd list: ").split()))
    head2 = create_linked_list(l2)
    head2.next.next = intersect_node

    intersection = get_intersection_node(head1, head2)
    
    if intersection:
        print("The lists intersect at node with data:", intersection.data)
    else:
        print("The lists do not intersect.")
