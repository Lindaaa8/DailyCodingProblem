// Q8 Solution


var hasCycle = function(head) {
    let hashSet = new Set();
    while (head !== null) {
        if (hashSet.has(head)) {
            return true;
        } else {
            hashSet.add(head);
        }
        head = head.next;
    }
    return false;
};