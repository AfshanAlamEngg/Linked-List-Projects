# Singly Linked List Implementation in Python

This implementation provides basic functionalities for a singly linked list, including insertion, deletion, and display of elements.

## Node Class
Represents a node in the linked list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## LinkedList Class
Manages the linked list operations.

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def delete(self, key):
        temp = self.head

        # If the head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # Key was not present in the linked list
        if temp == None:
            return

        # Unlink the node from the linked list
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

```

## Example Usage

``` python
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.display()  # Output: 1 2 3

    ll.delete(2)
    ll.display()  # Output: 1 3

    ll.delete(1)
    ll.display()  # Output: 3

```

##Explanation
1. Node Class: Represents a node in the linked list.
- __init__: Initializes the node with data and sets the next pointer to None.
2. LinkedList Class: Manages the linked list operations.
- __init__: Initializes the linked list with the head set to None.
- insert: Adds a new node with the specified data to the end of the list.
- delete: Removes the node containing the specified key from the list.
- display: Prints the elements in the list.

## Example Usage
- Create an instance of LinkedList.
- Insert elements (1, 2, 3) into the list.
- Display the list: 1 2 3.
- Delete the element 2 and display the list: 1 3.
- Delete the element 1 and display the list: 3.
