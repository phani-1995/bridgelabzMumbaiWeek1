# import random
#
# # function for coupon generation
# def CouponsGenerator(N_Coupons, Coupons_Range):
#     # 2 Lists are intialised with null
#     Coupons_list = []
#     Unique_list = []
#     count = 0
#     # transversed upto number of coupons generated
#     while len(Unique_list) != N_Coupons:
#         # adds the random numbers into list with in range
#         Coupons_list.append(random.randint(1, Coupons_Range))
#
#         # a unique set is extracted from coupon list
#         Unique_list = list(set(Coupons_list))
#
#         # counts the number of iterations to find required amount of distinct coupons
#         count = count + 1
#     # prints the coupon numbers from unique list
#     for Coupons_num in Unique_list:
#         CouponsGenerator(N_Coupons, Coupons_Range)
#         print(Coupons_num)
#
#     print("count is:", count)
#
# N_Coupons = int(input("Enter No of distinct coupon number: "))
# Coupons_Range = int(input("Enter the coupon range: "))
# CouponsGenerator(N_Coupons, Coupons_Range)
#




#################################################################################
import random

#function for coupoun generation
def CouponsGenerator(N_Coupons, Coupons_Range):
    # 2 Lists are intialised with null
    Coupons_list = []
    Unique_list = []
    count = 0
    # transversed upto number of coupons generated
    while len(Unique_list) != N_Coupons:
        # adds the random numbers into list with in range
        Coupons_list.append(random.randint(1, Coupons_Range))

        # a unique set is extracted from coupon list
        Unique_list = list(set(Coupons_list))

        # counts the number of iterations for to find required amount of distinct coupons
        count = count + 1
    # prints the coupon numbers from unique list
    for Coupons_num in Unique_list:
        print(Coupons_num)

    print("count is:", count)

if __name__ == '__main__':
    N_Coupons = int(input("Enter No of distinct coupon numbers: "))
    Coupons_Range = int(input("Enter max range:"))
CouponsGenerator(N_Coupons, Coupons_Range)