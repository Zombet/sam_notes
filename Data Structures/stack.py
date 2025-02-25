class Stack:
    def __init__(self, size=5):
        self.stk = []
        self.size = size
        print("Empty stack is created!")

    def push(self):
        if len(self.stk) == self.size:
            print("Stack Overflow")
            return
        element = input("Enter the element to be pushed: ")
        self.stk.insert(0, element)
        print(f"Element '{element}' pushed to stack.")

    def pop(self):
        if not self.stk:
            print("Stack is empty!")
            return
        print("Popped element is ", self.stk[0])
        del self.stk[0]

    def display(self):
        if not self.stk:
            print("Stack is empty!")
            return
        print("Stack elements are:", self.stk)


def menu():
    stack = Stack()
    while True:
        print("\nMenu:")
        print("1. Push element")
        print("2. Pop element")
        print("3. Display stack")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            stack.push()
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.display()
        elif choice == '4':
            print("Exiting the program. Thank you for using the stack!")
            break
        else:
            print("Invalid choice! Please try again.")


menu()

