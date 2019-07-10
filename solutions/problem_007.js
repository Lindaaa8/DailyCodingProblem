// Problem  7

var listSize = function(head) {
    let n = 0;
    while (head !== null) {
        n++;
        head = head.next;
    }
    return n;
}
var isPalindrome = function(head) {
    if (head === null || head.next === null) return true;
    let num = listSize(head);
    let half = Math.floor(num / 2);
    let remainder = num % 2 ? 1: 0;
    let prev = null;
    for (let i = 0; i < half; i++) {
        let temp = head.next;
        head.next = prev;
        prev = head;
        head = temp;
    }
    if (remainder) {
        head = head.next;
    }
    for (let j = 0; j < half; j++) {
        if (prev.val !== head.val) {
            
            return false;
        }
        prev = prev.next;
        head = head.next;
    }
    return true;
}