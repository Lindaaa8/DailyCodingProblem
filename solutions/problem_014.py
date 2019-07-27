from multiprocessing.dummy import Pool as ThreadPool 

class Solution:
    def interleavedString(a,b,c,a_i,b_i,c_i):
        len_a = len(a)
        len_b = len(b)
        len_c = len(c)
        a_i = b_i = c_i = 0
        if len_c != len_a + len_b:
            return False
        while c_i in range(len_c):
            if a[a_i] == c[c_i] and b[b_i] == c[c_i]:
                p
pool = ThreadPool(4) 
results = pool.map(my_function, my_array)

