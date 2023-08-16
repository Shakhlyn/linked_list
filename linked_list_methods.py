class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def push_node(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self
    
    def pop(self):
        if not self.head:
            return "undefined"
            
        current = self.head
        new_tail = self.head
        
        while current.next:
            new_tail = current
            current = current.next
        
        self.tail = new_tail
        self.tail.next = None
        self.length -=1
        return current
        
            
            # while current.next:
            #     current = current.next
            #     if current.next:
            #         new_tail = current
            #     self.tail = current
            # return new_tail
        
    def __str__(self):
        # return self.head, self.tail, self.length
        return f"Head: {self.head.data}, Tail: {self.tail.data}, Length: {self.length}"
            
            
new_list = SinglyLinkedList()
new_list.push_node('hi, ')
new_list.push_node('first')
new_list.push_node('Three')

print(new_list)
new_list.pop()
print(new_list)
new_list.pop()
print(new_list)
new_list.pop()
print(new_list)