# Singly Linked List Implementation in Python

This implementation provides basic functionalities for a singly linked list, including insertion, deletion, and display of elements.

## Node Class
Represents a node in the linked list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
