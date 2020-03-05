def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr=[90,70,100,99,85,74,63,72]
bubble_sort(arr)
for i in range(len(arr)):
    print(arr[i])
