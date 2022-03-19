# def multiply(num_list, num):
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# output:
# >>>[2,4,10,16]





# def multiply(num_list, num):
#     print(num_list, num)
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# output:
# >>>[2,4,10,16] 5
# >>>[2,4,10,16]

def one_through_ten(x):
    for i in range(1,x):
        if i % 2 == 0:
            print(i)
one_through_ten(10)