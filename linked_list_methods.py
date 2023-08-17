class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node   #assign 'new_node' to current tail's next
            self.tail = new_node        #Then, shift tail to 'new_node' from previous tail.
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
        if self.length == 0:
            self.head = None
            self.tail = None
        return current
    
    def shift(self):
        if not self.head:
            return 'Empty Linked List!!!'
        
        current = self.head
        self.head = current.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current
    
    def unshift(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current_head = self.head
            self.head = new_node
            new_node.next = current_head
        self.length +=1


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        counter = 0
        current = self.head
        while counter < index:
            current = current.next
            counter +=1
        # return current.value  #//if we want to print out only 'get()' method
        return current      # //We need to return node, current', because we will use later, i.e., in 'set()' method.
        # return current.value if current else None
    
    def set(self, index, value):
        old_node = self.get(index)
        if old_node:
            old_node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return 'Undefined'
        
        if index == 0:
            new_node = self.unshift(value)
            return new_node
        
        if index == self.length:
            new_node = self.push(value)
            return new_node
        
        prev_node = self.get(index -1)
        next_node = self.get(index)
        
        new_node = Node(value)
        prev_node.next = new_node
        new_node.next = next_node
        self.length += 1
        return new_node
    
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return 'Invalid index position!!!'
        
        elif index == 0:
            tobe_removed_node = self.shift()
        elif index == self.length -1:
            tobe_removed_node = self.pop()
        else:
            previous_node = self.get(index-1)
            tobe_removed_node = previous_node.next
            next_node = tobe_removed_node.next
            # next_node = previous_node.next.next
            
            
            previous_node.next = next_node
            self.length -= 1
        return tobe_removed_node
    
    
    def reverse(self):
        current_node = self.head
        previous_node = None
        self.tail = self.head
        self.head = self.tail
        
        for _ in range(self.length):
            previous_node = current_node
            current_node = current_node.next
            current_node.next = previous_node
            
        return self
    
        
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # To indicate the end of the list
    
    def __str__(self):
        if self.head is None:
            return f"Empty List: Undefined"
        return f"Head: {self.head.value}, Tail: {self.tail.value}, Length: {self.length}"
    
            
# *************************************************************
new_list = SinglyLinkedList()

new_list.push('One')
new_list.push('Two')
new_list.push('Three')
new_list.push('Four')

print(new_list)
new_list.print_list()

new_list.reverse()
print(new_list)
new_list.print_list()



# new_list.print_list()
# print(new_list.remove(-1))
# print(new_list)
# new_list.print_list()
# new_list.remove(0)
# print(new_list)
# new_list.print_list()
# print(new_list.remove(2).value)
# print(new_list)
# new_list.print_list()

# print(new_list.remove(3))
# print(new_list)
# new_list.print_list()



# new_list.insert(0, 'inserted-new-value')
# print(new_list)
# new_list.insert(3, 'last')
# new_list.print_list()
# print(new_list)
# new_list.insert(5, 'last')
# new_list.print_list()
# print(new_list)


# new_list.set(0, 'new')
# print(new_list)
# new_list.print_list()


# below = new_list.get(-1)
# first = new_list.get(0)
# second = new_list.get(1)
# third = new_list.get(2)
# fourth = new_list.get(3)
# new_list.print_list()
# print(f"below: {below}, first: {first.value}, second: {second.value}, third: {third.value}, fourth: {fourth}")


# print(new_list.get(-1))
# print(new_list.get(0))
# print(new_list.get(1))
# print(new_list.get(2))
# print(new_list.get(3))



# new_list.unshift('begin')
# new_list.unshift('Pre-begin')
# print(new_list)

# new_list.shift()
# new_list.shift()
# new_list.shift()
# print(new_list)

# new_list.pop()
# print(new_list)
# new_list.pop()
# print(new_list)
# new_list.pop()
# print(new_list)
