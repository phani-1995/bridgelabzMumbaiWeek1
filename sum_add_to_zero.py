def sum_add_to_zero(arr):
    n=len(arr)
    arr=sorted(arr)
    found=False
    for i in range(0,n-1):
        low=i+1
        high=n-1
        while low<high:
            if (arr[i]+arr[low]+arr[high] == 0):
                print(arr[i],arr[low],arr[high])
                found=True
            elif (arr[i]+arr[low]+arr[high]<0):
                low+=1
            else:
                high-=1
    if found == False:
        print("no numbers found")
n=int(input("Enter the length of array: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter the elements of array: ")))
sum_add_to_zero(arr)


