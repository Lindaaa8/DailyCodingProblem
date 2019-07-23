var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let end = n;
        let begin = 1;
        let mid = Math.floor(begin+end)/2;
        while (end > begin) {
            
            let res1 = isBadVersion(mid);
            if (res1) {
                end = mid;
            } else {
                begin = mid+1;
            }
            let res = Math.floor((begin+end)/2);
            if (mid === res) break;
            mid = res;
        }
        return mid;
    };
};