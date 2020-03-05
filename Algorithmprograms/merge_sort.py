def mergesort(alist):
    print("splitting",alist)
    if len(alist)>1:
        mid=len(alist)//2
        left_half=alist[mid: ]
        right_half=alist[ :mid]
        mergesort(left_half)
        mergesort(right_half)
        i=0
        j=0
        k=0
        while i<=len(left_half) and j<len(right_half):
            if left_half[i]<=right_half[j]:
                alist[k]=left_half[i]
                i+=1
            else:
                alist[k]=right_half[j]
                j+=1
            k+=1
            while j<len(right_half):
                alist[k] = right_half[j]
                j=j+1
                k=k+1
            print("Merging",alist)

def printList(alist):
    for i in range(len(alist)):
        print(alist[i], end='')
    print()
alist = ["Cricket","Football","Throwball","Basket ball","Kabbadi"]
mergesort(alist)