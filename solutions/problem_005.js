

var check_balance = function(tree,min,max) {
    if (tree === null) return true;
    let a = tree.val;
    let b = tree.left;
    let c = tree.right;
    if (b && a <= b.val || c && a >= c.val) {
        return false;
    }
    if (min && a <= min || max && a >= max) {
        return false;
    }
    return check_balance(b, min,a) && check_balance(c, a,max);
}
var isValidBST = function(root) {
    return check_balance(root,null,null);
}