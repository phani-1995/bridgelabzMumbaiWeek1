def binary_search(word,word_list):
    first=0
    last=len(word_list)-1
    found=False
    while first<=last and not found:
        middle=(last+first)//2
        if word_list[middle] == word:
            found=True
        elif word<word_list[middle]:
            last=middle-1
        else:
            first=middle+1
        return found
    if found == True:
        print("The word is their in the list")
    else:
        print("The word is not present in the list")

word_list=["Apple","Grapes","Mango","Banana","Orange","Water melon"]
word=input("Enter the word to search: ")
binary_search(word,word_list)

#########################################################################
# def binary_search(A,key):
#     lower_ind=0
#     upper_ind=len(A)-1
#     while lower_ind <= upper_ind:
#         middle_ind=(lower_ind+upper_ind)//2
#         if A[middle_ind] == key:
#             return True
#         elif A[middle_ind]>key:
#             upper_ind=middle_ind-1
#         else:
#             A[middle_ind]<key
#             lower_ind=middle_ind+1
# A=["Apple","Mango","Banana","Grapes","PineApple"]
# key=input("Enter the word to search: ")
# binary_search(A,key)