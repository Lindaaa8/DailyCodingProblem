function loopthrough(str,s) {
    for (let i = 0; i < str.length; i++) {
        if (str[i] === s) return i;
    }
    return -1;
}
var lengthOfLongestSubstring = function(s) {
    var array = [];
    var searchable = '';
    for (let i = 0; i < s.length; i++) {
        let ind = loopthrough(searchable,s[i]);
        if (ind === -1) {
            searchable = searchable + s[i];
        } else {
            array.push(searchable.length);
            searchable = searchable.substring(ind+1,i) + s[i];
        }
    }
    array.push(searchable.length);
    return Math.max(...array);
};