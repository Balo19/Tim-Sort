import random
MIN_MERGE = 32
 
def calcMinRun(n):
    """Gibt die minimale Länge eines
    Laufs von 23 - 64 zurück, so dass
    len(array)/minrun kleiner als oder gleich
    gleich einer Potenz von 2 ist.

    z.B. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
 
# Diese Funktion sortiert das Array vom linken Index bis
# bis zum rechten Index, der die Größe atmost RUN hat
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
 
 
# Merge-Funktion führt die sortierten Läufe zusammen
def merge(arr, l, m, r):
 
    # Das ursprüngliche Array ist in zwei Teile aufgeteilt
    # linkes und rechtes Array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
 
    i, j, k = 0, 0, l
 
    # nach dem Vergleich werden die beiden Felder zusammengeführt
    # in einem größeren Unterfeld
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
 
        else:
            arr[k] = right[j]
            j += 1
 
        k += 1
 
    # Verbleibende Elemente von links kopieren, falls vorhanden
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
 
    # Ggf. verbleibendes Element von rechts kopieren
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
 
 
# Iterative Timsort-Funktion zum Sortieren des
# Array[0...n-1] (ähnlich wie Merge Sort)
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
 
    # Sortieren individuellen subarrays von der grösse des RUNs
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
 
    # Beginnen Sie das Zusammenführen ab Größe RUN (oder 32). Es wird zusammengeführt
    # zur Größe 64, dann 128, 256 und so weiter ....
    size = minRun
    while size < n:
 
        # Wählen Sie den Startpunkt des linken Subarrays. Wir
        # werden arr[left..left+size-1] verschmelzen
        # und arr[left+size, left+2*size-1]
        # Nach jeder Zusammenführung erhöhen wir left um 2*size
        for left in range(0, n, 2 * size):
 
            # Endpunkt des linken Unterfeldes finden
            # Mitte+1 ist der Startpunkt des rechten Unterfeldes
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            # Sub-Array arr[left.....mid] zusammenführen &
            # arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)
 
        size = 2 * size
 
 
# Driver program zum Testen der obigen Funktion
if __name__ == "__main__":
    arr = []
    for i in range(1000):
        arr.append(random.randint(0, 100))
 
    print("Given Array is")
    print(arr)
 
    # Funktion aufrufen
    timSort(arr)
 
    print("After Sorting Array is")
    print(arr)