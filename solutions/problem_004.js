var removeNthFromEnd = function(head, n) {
    let another = new ListNode(0);
    another.next = head;
    let first = another;
    let second = another;
    for (let i = 0; i < n; i++) {
        first = first.next;
    }
    while (first.next !== null) {
        first = first.next;
        second = second.next;
    }
    if (second.next !== null) {
        second.next = second.next.next;
    } 
    return another.next;
};



// step 2: Could you do this in one pass?

