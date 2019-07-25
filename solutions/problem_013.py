class ListNode():
    # Function to initialise the node object
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        node = self
        output = ""
        while node:
            output += str(node.data) + " "
            node = node.next
        return output

def list2linkedlist(l):
    if l == []:
        return None
    head = ListNode(l[0])
    n = head
    for i in range(1,len(l)):
        node = ListNode(l[i])
        n.next = node 
        n = n.next
    return head

    # reverse a linked list iteratively
def reverse(node):
    cur = node
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
# reverse a linked list iteratively

def reverseR(prev,node):
    curr = node
    if curr == None:
        return prev
    next = curr.next
    curr.next = prev
    return reverseR(curr,next)
    
def reverse2(node):
    return reverseR(None,node)
def removeEle(node,num):
    cur = node
    next = None
    prev = None
    found = False
    while cur:
        next = cur.next
        if (cur.data == num or found) and next != None:
            found = True
            cur.data = next.data
            if not next.next:
                cur.next = None
        if cur.data == num and next == None:
            cur = None
            break
        cur = next
    return node

if __name__ ==  '__main__':
    l1 = [1,2,3,4,5]
    linkedlist1 = list2linkedlist(l1)
    linkedlist3 = reverse2(linkedlist1)
    print(linkedlist3)
    result = removeEle(linkedlist3,4)
    print(result)
    print(linkedlist3)
    print('done')

