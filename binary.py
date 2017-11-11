def binary_search(arr, l, r, x):
    print(x,r,l)
    if r >= l:
        mid = l+(r-l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid-1, x)
        else:
            return binary_search(arr, mid+1, r, x)
    else:
        return -1
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("enter element to search: "))

result = binary_search(arr, 0, len(arr)-1, x)

if result == -1:
    print("element is not present")
else:
    print("element present at index  %d" %result)

