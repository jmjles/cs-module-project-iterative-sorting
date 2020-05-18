# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        current = i
        smallest_index = 0
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for x in range(smallest_index,len(arr)):
            if(arr[current] < arr[x]):
                arr[current], arr[x] = arr[x], arr[current]
        smallest_index+=1
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for x in range(0,len(arr) - 1):
        for y in range(0,len(arr)-1):
            if (arr[y] > arr[y+1]):
                arr[y],arr[y+1] = arr[y+1],arr[y]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
