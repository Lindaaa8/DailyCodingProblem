// dynamic programming proach (use two variables a and b instead of Array(n) to store the previous results)


var climbStairs = function(n) {
    if (n === 1|| n === 0) return 1;
    let a = b = 1;
    while (n >= 2) {
        a = a + b;
        b = a-b;
        n--;
    }    
    return a;
    
};


// Time Complexity O(n)

// Space Complexity O(1) 
