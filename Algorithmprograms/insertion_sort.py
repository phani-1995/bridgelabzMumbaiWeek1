def insertion_sort(my_list):
    for i in range(1,len(my_list)):
        pos=i
        current_element=my_list[pos]
        while current_element> my_list[pos-1] and pos>0:
            my_list[pos] = my_list[pos-1]
            pos=pos-1
            my_list[pos]=current_element
my_list=["Apple","PineApple","Banana","Grapes","Orange"]
insertion_sort(my_list)
print(my_list)