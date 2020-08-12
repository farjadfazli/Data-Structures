"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        if self.prev:
            self.prev.next = node.next
        if node.next:
            self.next.prev = node.prev

            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        self.length -= 1
        if self.head == self.tail:
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        else:
            val = self.head.value
            self.head = self.head.next
            return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return None
        self.length -= 1
        if self.head == self.tail:
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        else:
            val = self.tail.value
            self.tail = self.tail.prev
            return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    # combining the move_to_front and move_to_end methods
    def move(self, node, front):
        name = "head" if front else "tail"
        if getattr(self, name) == node:
            return None

        opposite_name = "tail" if front else "head"

        if getattr(self, opposite_name) == node:
            setattr(self, opposite_name, node.prev if opposite_name == "tail" else node.next)
            setattr(getattr(self, opposite_name), "next" if name == "head" else "prev", None)

        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        setattr(getattr(self, name), "prev" if name == "head" else "next", node)
        setattr(node, "next" if name == "head" else "prev", getattr(self, name))
        setattr(self, name, node)

    def move_to_front(self, node):
        self.move(node, True)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.move(node, False)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None and self.tail is None:
            return
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None and self.tail is None:
            return None
        max_value = self.head.value
        current = self.head.next

        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value