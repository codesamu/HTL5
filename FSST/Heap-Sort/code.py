import random
import time

n = 20000
zahlen = random.sample(range(n * 10), n)

def heapify(arr, n, i):
    groesstes = i
    links = 2*i + 1
    rechts = 2*i + 2

    if links < n and arr[links] > arr[groesstes]:
        groesstes = links
    if rechts < n and arr[rechts] > arr[groesstes]:
        groesstes = rechts

    if groesstes != i:
        arr[i], arr[groesstes] = arr[groesstes], arr[i]
        heapify(arr, n, groesstes)

def heap_sort(arr):
    n = len(arr)

    # Max-Heap aufbauen
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Größtes Element nach hinten
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

start = time.perf_counter()
heap_sort(zahlen)
ende = time.perf_counter()

print("Laufzeit:", ende - start, "Sekunden")
