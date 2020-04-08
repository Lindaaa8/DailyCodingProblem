#!/usr/bin/env python3

class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        l = self
        output = ""
        while l != None:
            output += str(l.data) + " "
            l = l.next
        return output
    
def removeElement(node, e):
    l = node
    first = LinkedList(1)
    first.next = l
    prev = first
    if l == None:
        return l
    while l and l.next != None:
        if (l.data != e):
            first.next = l
            first = first.next
        else: 
            l = l.next
            if (l.data != e):
                first.next.data = l.data
                first = first.next  
        l = l.next
    if (l and l.data == e): first.next = None
    else: first.next = l
    return prev.next
        
def list2linkedlist(l):
    node = LinkedList(1)
    prev = node
    for i in l:
        nextNode = LinkedList(i)
        node.next = nextNode
        node = node.next
    return prev.next

def reverse(node):
    prev = None
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    return prev
def oddFollowedByEven(l):
    if l == None: return l
    copy = l
    second = LinkedList(1)
    copy2 = second
    while l.next != None:
        second.next = l.next
        second = second.next
        next = second.next
        if next != None:
            l.next = next
            l = l.next
        else: 
            l.next = copy2.next
            return copy
    second.next = None
    l.next = copy2.next
    return copy

def isPalindrome(l):
    first = LinkedList(1)
    copy = l
    first.next = copy
    length = 0
    while l != None:
        length += 1
        l = l.next
    count = length // 2 + length % 2
    for i in range(1,count):
        copy = copy.next
    copy.next = reverse(copy.next)
    while copy.next != None:
        first = first.next
        copy = copy.next
        if first.data != copy.data:
            return False
    return True

if __name__ == "__main__":
    list1 = [7,1,3,4,7,7,5,2,7]
    list2 = [7,1]
    list3 = [7]
    list4 = [1,23,4,5,3]
    list5= [1,2,3,4,6,7]
    list6 = [1,2,2,2,1]
    list7=[]
    ll1 = list2linkedlist(list6)
    print(ll1)
    print(isPalindrome(ll1))

