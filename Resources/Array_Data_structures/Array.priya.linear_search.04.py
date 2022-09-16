## Searching Algorithm - Linear Search
## Time Complexity - O(n)[One for loop]
def linearSearch(arr, search_element, n):
    for i in range(n):
        if arr[i] == search_element:
            return i
    ## Element is not present inside the array
    return -1

arr = [53, 12, 32, 17, 39, 90]
search_element = 17
n = len(arr)
result = linearSearch(arr, search_element, n)
print("Search Element index is", result)
