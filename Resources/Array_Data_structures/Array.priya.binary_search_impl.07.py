## Implementation Of Binary Search Algorithm using Recursion Technique
## Time Complexity - O(log N)
## Try to implement Binary Search without using recursion(Iterative Approach)
def binarySearch(array, i, j, x):
    ## Single Element Search
    if i == j:
        if array[i] == x:
            return i
        else:
            return -1
    else:
        mid = i + (j-i) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            ## Recursive Call
            return binarySearch(array, mid+1, j, x)
        else:
            ## Recursive Call
            return binarySearch(array, i, mid-1, x)
## Driver code
array = [10, 23, 35, 67, 75, 86, 90]
i = 0
j = len(array) - 1
x = 86
result = binarySearch(array, i, j, x)
print("Searching value is present at index", result)