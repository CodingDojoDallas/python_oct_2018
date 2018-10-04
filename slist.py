class Node():
    def __init__(self, val, next=None):
        self.val  = val
        self.next = next

class SList():
    def __init__(self, value):
        self.head = Node(value)

    def add(self, value):
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(value)
        return self

    def remove(self, value):
        current = self.head
        previous = None
        while current:
            if current.val == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = None
                return self
            current = current.next
            prev = current
        return self

    def display(self):
        ptr = self.head
        while ptr:
            print('Value: ', ptr.val, 'Next:', ptr.next)
            ptr = ptr.next
        return self

s = SList(4)
s.add(10)
s.add(17)
s.remove(17)
s.remove(4)
s.remove(10)
s.remove(11)
s.display()
