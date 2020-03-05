def anagram(str1,str2):
    x=sorted(str1)
    y=sorted(str2)
    if (x == y):
        print("The given strings are anagram")
    else:
        print("The given strings are not anagram")
str1=input("Enter the string: ")
str2=input("Enter the string: ")
anagram(str1,str2)