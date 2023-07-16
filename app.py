print('Hello world')

class MyClass:
    x = 20


p = MyClass()

class Person: 
    def __init__(self,name,age):
        self.name = name
        self.age = age

        getattr(self, 'name', None)
p1 = Person('Tanvir Hossain',20)


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
            self.head.next = node
            node.prev = self.head
            self.tail = node
            self.size += 1
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
my_list.add(2)

print(my_list)
