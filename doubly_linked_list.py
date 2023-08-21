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
            
            
    def get(self, index):
        if index < 0 or index >= self.length:
            return 'Invalid index position!'
        
        elif index <= self.length/2:
            counter = 0
            current = self.head
            while counter != index:
                current = current.next
                counter += 1
        else:
            counter = self.length -1
            current = self.tail
            while counter != index:
                current = current.prev
                counter -=1
        return current
            
            
    def set(self, index, value):
        if index < 0 or index >= self.length:
            return "Invalid index position!"
        else:
            tobe_node = self.get(index)
            tobe_node.value = value
            return True
        
        
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return "Invalid index position"
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            next_node = self.get(index)
            previous_node = next_node.prev
            previous_node.next = new_node
            new_node.prev = previous_node
            new_node.next = next_node
            next_node.prev = new_node
            self.length += 1

  
    def reverse(self):
        current_node = self.head
        self.head = self.tail
        self.tail = current_node
        
        previous_node = None
        
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            current_node.prev = next_node
            
            previous_node = current_node
            current_node = next_node
                    
        return self
    
    
    def array_to_doubly_linked_list(self, array):
        for item in array:
            self.append(item)

        
    def __str__(self):
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

# doubly_linked_list.append('old')
# doubly_linked_list.append('new_value')
# doubly_linked_list.append('extra')
# doubly_linked_list.append('ultra')

doubly_linked_list.array_to_doubly_linked_list(['hi', 6, 23.44, 'new string', 'last'])

print(doubly_linked_list)
doubly_linked_list.print_list()

doubly_linked_list.reverse()
print(doubly_linked_list)
doubly_linked_list.print_list()

# doubly_linked_list.insert(0, "first")
# doubly_linked_list.insert(23, "exceeds")
# doubly_linked_list.insert(2, "third")
# print(doubly_linked_list)
# doubly_linked_list.print_list()

# print(doubly_linked_list.set(-1, 'first node'))
# print(doubly_linked_list.set(0, 'first node'))
# # print(doubly_linked_list.set(2, 'two'))
# print(doubly_linked_list)
# doubly_linked_list.print_list()

# print(doubly_linked_list.get(0).value)
# print(doubly_linked_list.get(1).value)
# print(doubly_linked_list.get(3).value)
# print(doubly_linked_list.get(2).value)

# doubly_linked_list.shift()
# print(doubly_linked_list)
# doubly_linked_list.print_list()
# doubly_linked_list.shift()
# print(doubly_linked_list)
# doubly_linked_list.print_list()
# doubly_linked_list.shift()
# print(doubly_linked_list)
# doubly_linked_list.print_list()
# doubly_linked_list.shift()
# print(doubly_linked_list)
# doubly_linked_list.print_list()
# doubly_linked_list.shift()
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
# doubly_linked_list.pop()
# print(doubly_linked_list)
# doubly_linked_list.print_list()

# doubly_linked_list.prepend('old')
# doubly_linked_list.prepend('new_value')
# doubly_linked_list.prepend('extra')
# doubly_linked_list.prepend('ultra')

