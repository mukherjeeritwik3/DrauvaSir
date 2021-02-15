def get_max(a, compare):
    largest = a[0]
    for item in a[1:]:
        if compare(item,largest):
            largest = item
    return largest

def bubbleSort(a, compare):
    for item in range(len(a)-1,0,-1):
        for items in range(item):
            if compare(a[items],a[items+1]):
                a[items], a[items+1] = a[items+1], a[items]
    return a
def selctionSort(a, compare):
    for i in range(len(a)):
        minpos = i
        for j in range(i, len(a)):
            if compare(a[minpos],a[j]):
                minpos = j
    
        a[i], a[minpos] = a[minpos], a[i]
    return a    

## Error with selection sort