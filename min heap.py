heap = []
def parent(i):
    return (i-1)>>1

def leftf(i):
    return (i << 1) + 1

def rightf(i):
    return (i << 1) + 2

def heapify_down(i):
    global heap
    smallest = i
    left = leftf(i)
    right = rightf(i)
    n = len(heap)

    if left < n and heap[left] < heap[smallest]:
        smallest = left

    if right < n and heap[right] < heap[smallest]:
        smallest = right

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        heapify_down(smallest)

def build_min_heap(array):
    global heap
    heap = array
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(i)

def heapify_up(i):
    global heap
    while i > 0 and heap[parent(i)] > heap[i]:
        parent_index = parent(i)
        heap[i], heap[parent_index] = heap[parent_index], heap[i]
        i = parent_index

def push(value):
    global heap
    heap.append(value)
    heapify_up(len(heap) - 1)

def pop():
    global heap
    if not heap:
            return None
    root = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    heapify_down(0)
    return root


build_min_heap([4, 10, 3, 5, 1])
print(heap)  
print(pop())  
print(heap)  
push(2)
print(heap)  
