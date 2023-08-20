class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            # self.length += 1
        else:
            old_tail = self.tail
            self.tail = new_node
            old_tail.next = new_node
            new_node.prev = old_tail
        self.length += 1
        
    
    def prepend(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            self.head = new_node
            new_node.next = old_head
            old_head.prev = new_node
    
        self.length += 1
        
        
    def pop(self):
        if not self.head:
            print("This method is not applicable because there is no node")
        
        elif not self.head.next:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            old_tail = self.tail
            self.tail = old_tail.prev
            old_tail.prev = None            
            self.tail.next = None
            self.length -= 1
            
    def shift(self):
        if self.length == 0:
            print('This method is not applicable because there is no node')
        elif self.length  == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            old_head = self.head
            self.head = old_head.next
            old_head.next = None
            self.head.prev = None
            self.length -= 1
            
        
    def __str__(self) -> str:
        if self.head is None:
            return f"Empty List: Undefined"
        return f"Head: {self.head.value}, Tail: {self.tail.value}, Length: {self.length}"

    def print_list(self):
        if self.length > 0:
            current = self.head
            while current:
                print(current.value, end=" -> ")
                current = current.next
            print('NONE')
        else:
            print('No node present')
        print("------------------------")

doubly_linked_list = DoublyLinkedList()

doubly_linked_list.append('old')
doubly_linked_list.append('new_value')
doubly_linked_list.append('extra')
doubly_linked_list.append('ultra')

print(doubly_linked_list)
doubly_linked_list.print_list()


doubly_linked_list.shift()
print(doubly_linked_list)
doubly_linked_list.print_list()
doubly_linked_list.shift()
print(doubly_linked_list)
doubly_linked_list.print_list()
doubly_linked_list.shift()
print(doubly_linked_list)
doubly_linked_list.print_list()
doubly_linked_list.shift()
print(doubly_linked_list)
doubly_linked_list.print_list()
doubly_linked_list.shift()
print(doubly_linked_list)
doubly_linked_list.print_list()

# doubly_linked_list.pop()
# print(doubly_linked_list)
# doubly_linked_list.print_list()
# doubly_linked_list.pop()
# print(doubly_linked_list)
# doubly_linked_list.print_list()
# doubly_linked_list.pop()
# print(doubly_linked_list)
# doubly_linked_list.print_list()
# doubly_linked_list.pop()
# print(doubly_linked_list)
# doubly_linked_list.print_list()
# doubly_linked_list.pop()
# print(doubly_linked_list)
# doubly_linked_list.print_list()

# doubly_linked_list.prepend('old')
# doubly_linked_list.prepend('new_value')
# doubly_linked_list.prepend('extra')
# doubly_linked_list.prepend('ultra')

