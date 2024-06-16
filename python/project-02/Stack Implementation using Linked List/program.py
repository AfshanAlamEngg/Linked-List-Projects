
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} to the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack underflow! Cannot pop from an empty stack.")
            return None
        popped_node = self.top
        self.top = self.top.next
        print(f"Popped {popped_node.data} from the stack.")
        return popped_node.data

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        print(f"Top element is {self.top.data}.")
        return self.top.data

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())  # Output: 30
print(stack.pop())   # Output: 30
print(stack.pop())   # Output: 20
print(stack.pop())   # Output: 10
print(stack.pop())   # Output: None (Stack underflow)
