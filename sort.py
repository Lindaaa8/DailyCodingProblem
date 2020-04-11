
def bubbleSort(l):
    length = len(l)
    for i in range(length):
        for j in range(i+1,length):
            if l[j] < l[i]:
                l[j],l[i] = l[i], l[j]
    return l
def insertionSort(l):
    n = len(l)
    i = 0
    while i < n:
        temp = l[i]
        for j in range(i+1,n):
            if l[i] > l[j]:
                l[j],l[i] = l[i], l[j]
                break
        if l[i] == temp:
            i += 1
    return l

def quickSort(arr):
    return quickSortHelper(arr,0,len(arr)-1)

def quickSortHelper(arr,l,h):
    if h <= l:
        return arr
    p = partition(arr,l,h)
    quickSortHelper(arr,l,p-1)
    quickSortHelper(arr,p+1,h)
    return arr

def partition(arr,l,h):
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1

def mergeSort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    mid = length//2
    L = arr[:mid]
    R = arr[mid:]
    a = mergeSort(L)
    b = mergeSort(R)
    i = j = 0
    for index in range(length):
        if i == len(b):
            arr[index] = a[j]
            j += 1
        elif j == len(a):
            arr[index] = b[i]
            i += 1
        elif b[i] < a[j]:
            arr[index] = b[i]
            i += 1
        else:
            arr[index] = a[j]
            j += 1
    return arr


if __name__ == "__main__":
    l = [9,32,4,6,8,4,1]
    l2 = [9]
    l3 = [32,9]
    l1 = []
    print(l[:len(l)//2])
    print(insertionSort(l1))
    print(insertionSort(l))
    print(insertionSort(l2))
    print(insertionSort(l3))
    print(mergeSort(l1))
    print(mergeSort(l))
    print(mergeSort(l2))
    print(mergeSort(l3))