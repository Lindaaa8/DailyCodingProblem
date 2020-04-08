class Node:
    def __init__(self, data, prev, next):
        self.prev = prev
        self.next = next
        self.data = data
    def __str__(self):
        l = self
        output = ""
        while l != None:
            output += str(l.data) + " "
            l = l.next
        return output
class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index):
        node = self.head
        count = 0
        while node != None:
            if (count == index):
                return node.data
            count += 1
            node = node.next
        return -1
    
    def addAtHead(self,val):
        node = self.head
        head = Node(val, None, node)
        if node != None:
            node.prev = head
        else: self.tail = head
        self.head = head
    
    def addAtTail(self,val):
        node = self.tail
        tail = Node(val,node,None)
        if node != None:
            node.next = tail
        else: self.head = tail
        self.tail = tail

    def addAtIndex(self, index, val):
        node = self.head
        count = 0
        while node != None:
            if (count == index):
                newNode = Node(val,node.prev,node)
                next = node.next
                node.prev.next = newNode
                if node.prev == None: self.head = newNode
                node.prev = newNode
                if next == None: self.tail = node
                return
            count += 1
            node = node.next
        if (count == index): self.addAtTail(val)

    def deleteAtIndex(self, index):
        node = self.head
        count = 0
        while node != None:
            if (count == index):
                prev = node.prev
                next = node.next
                if prev != None: node.prev.next = next
                else: self.head = next
                if next != None: node.next.prev = prev
                else : self.tail = prev
                node.next = None
                node.prev = None
            node = node.next
            count = count + 1

if __name__ == "__main__":
    ll1 = doublyLinkedList()
    print(ll1.get(3))
    print(ll1.head, "and", ll1.tail)
    ll1.addAtHead(3)
    print(ll1.head, "and", ll1.tail)
    ll1.addAtTail(4)
    print(ll1.head, "and", ll1.tail)
    ll1.addAtTail(47)
    print(ll1.head, "and", ll1.tail)
    ll1.addAtHead(1)
    print(ll1.head, "and", ll1.tail)
    ll1.addAtIndex(2,6)
    print(ll1.head, "and", ll1.tail)
    ll1.addAtIndex(5,3)
    print(ll1.head, "and", ll1.tail)
    ll1.addAtHead(1)
    print(ll1.head, "and", ll1.tail)
    ll1.deleteAtIndex(0)
    print(ll1.head, "and", ll1.tail)
    ll1.deleteAtIndex(4)
    print(ll1.head, "and", ll1.tail)
    ll1.deleteAtIndex(5)
    print(ll1.head, "and", ll1.tail)
    ll1.deleteAtIndex(2)
    print(ll1.head, "and", ll1.tail)
    ll1.deleteAtIndex(3)
    print(ll1.head, "and", ll1.tail)
