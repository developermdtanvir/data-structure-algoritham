"""

# Datastcture for the node list


"""

class Node: 
    def __init__(self,value):
        self.next = None
        self.prev = None
        self.val = value

class DubbleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def add(self,value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node 
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.head
            self.tail = node
            self.size += 1
    
    def __remove_node(self,node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        
        self.size -= 1

    def remove(self,value):
        node = self.head
        while node is not None: 
            if node.val == value:
                self.__remove_node(node)
                break
            node = node.next

    def remove__first(self):
        if self.tail is not None:
            self.__remove_node(self.head)
        


    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{','.join(str(val) for val in vals)}]"


my_list = DubbleLinkList()
my_list.add(1)
my_list.add(5)
my_list.add(5)
my_list.add(5)
my_list.add(5)
my_list.add(5)
my_list.remove(5)
my_list.remove(5)

my_list.remove__first()
print(my_list)

print(my_list.size)
