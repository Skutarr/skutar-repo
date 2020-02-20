# def possitive_sum(arr):
#     new_arr=0
#     for x in arr:
#         if x>0:
#             new_arr=new_arr+x
#         # else:
#         #     print("all negat")
#         #     return 0
#     print((new_arr))
#     return new_arr
#
#
Numb_array= [1,2,-3,4]
# possitive_sum(Numb_array)

def possitive_sum(arr):
    new_arr=0
    for x in arr:
        if x>0 :
            new_arr=new_arr+x
    return  new_arr

possitive_sum(Numb_array)
