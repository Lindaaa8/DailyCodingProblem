const reverse = (prev, cur) => {
    let tmp = cur.next;
    cur.next = prev;
    prev = cur;
    if (tmp) {
        return reverse(prev,tmp);
    } else {
        return prev;
    }
}
var reverseList = function(head) {
    if (!head) return head;
    let prev = null;
    return reverse(prev,head);
}