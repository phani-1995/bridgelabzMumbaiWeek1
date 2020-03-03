def TwoDArray(rows, cols):
    # created an array with row * col size
    arry = [[0 for i in range(cols)] for j in range(rows)]

    # initialising array with int,double and bool type dynamically
    for i in range(rows):
        for j in range(cols):
            arry[i][j] = float(input("Enter float value:"))
            j = j + 1
            arry[i][j] = int(input("Enter int value"))
            j = j + 1
            arry[i][j] = bool(input("Enter bool value"))
            break
    # prints the two dimensional array
    for i in range(rows):
        for j in range(cols):
            print(arry[i][j],end=' ')
            # print(type(arr[i][j]))
        print()

TwoDArray(5,5)
# if __name__ == '__main__':
#     TwoDArray(3, 3)

############################
