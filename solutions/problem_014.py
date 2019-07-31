

import numpy

def interleavedString(a,b,c):
    len_a = len(a)
    len_b = len(b)
    len_c = len(c)
    twoDarray = numpy.empty((10, 10))
    twoDarray.fill(False)
    if len_c != len_a + len_b:
        return False
    for i in range(len_a+1):
        for j in range(len_b+1):
            if i == 0 and j == 0:
                twoDarray[0][0] = True
            elif b[j-1] == c[j-1] and i == 0:
                twoDarray[0][j] = twoDarray[0][j-1]
            elif a[i-1] == c[i-1] and j == 0:
                twoDarray[i][j] = twoDarray[i-1][j]
            elif b[j-1] == c[i+j-1] and a[i-1] != c[i+j-1]:
                twoDarray[i][j] = twoDarray[i][j-1]
            elif a[i-1] == c[i+j-1] and b[i-1] != c[i+j-1]:
                twoDarray[i][j] = twoDarray[i-1][j]
            elif a[i-1] == c[i+j-1] and b[i-1] == c[i+j-1]:
                twoDarray[i][j] = twoDarray[i-1][j] or twoDarray[i][j-1]
    return twoDarray[len_a][len_b]

if __name__ ==  '__main__':
    s1 = 'ACCABBCDA'
    s2 = 'BACEDAF'
    s3 = 'BACCAACEBBCDADAF'
    result = interleavedString(s1,s2,s3)
    print(result)

