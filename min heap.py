heap = []
def parent(i):
    return (i-1)>>1

def leftf(i):
    return (i << 1) + 1

def rightf(i):
    return (i << 1) + 2

def heapify_down(i):
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
    while i > 0 and heap[parent(i)] > heap[i]:
        parent_index = parent(i)
        heap[i], heap[parent_index] = heap[parent_index], heap[i]
        i = parent_index

def push(value):
    heap.append(value)
    heapify_up(len(heap) - 1)

def pop():
    if not heap:
            return None
    root = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    heapify_down(0)
    return root

print("example-1")
build_min_heap([5, 11, 4, 6, 2])
print("Min heap: ",heap)  
print("element popped: ",pop())  
print("heap after pop: ",heap)  
print("element to be pushed: 9")
push(9)
print("heap after push: ",heap)  
print()
print("example-2")
build_min_heap([3, 2.46, 4, 10, 1.1])
print("Min heap: ",heap)  
print("element popped: ",pop())  
print("heap after pop: ",heap)  
print("element to be pushed: 9")
push(2)
print("heap after push: ",heap)  
