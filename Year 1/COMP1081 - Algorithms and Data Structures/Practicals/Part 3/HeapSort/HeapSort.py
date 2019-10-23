def Heapify(A,n,v):
    largest=v
    if 2*v+1 < n and A[2*v+1]>A[v]:
        largest=2*v+1
    if 2*v+2 < n and A[2*v+2]>A[largest]:
        largest=2*v+2
    if largest != v:
        A[v],A[largest]=A[largest],A[v]
        Heapify(A,n,largest)


def BuildHeap(A,n):
    for i in range(n, -1, -1):
        Heapify(A, n, i)

def heapSort(A):
    n = len(A)

    BuildHeap(A,n)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        Heapify(A, i,0)
    return A

print(heapSort([1,6,3,2,4,3,8,7,4]))

