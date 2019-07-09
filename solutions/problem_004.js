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

var removeNthFromEnd = function(head, n) {
    let new_head = new ListNode(0);
    new_head.next = head;
    let prev = cur = new_head;
    let num = 0;
    while (cur.next !== null) {
        if (num < n) {
            num++;
            cur = cur.next;
        } else {
            cur = cur.next;
            prev = prev.next;
        }
    }
    if (prev.next !== null) {
        prev.next = prev.next.next;
    }
    return new_head.next;
}