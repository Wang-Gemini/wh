# def user_info(*args):
#     print(args)

# user_info('TOM')
# user_info('TOM',18)

# def user_info(**kwargs):
#     print(kwargs)
#
# user_info(name='TON',age=18,id=110)

# 定义一个函数，可以求任意个数字（个数）的和
# def sum(*nums):
#     result=0
#     for n in nums:
#         result +=n
#     print(result)
#
# sum(123,456,789,10,20,30,40)

# 定义一个函数，可以求任意个数字的平均值
def cacluate(*args):
    sun_num=sum(args)
    print(sun_num)
    ave_num=int(sum(args)/len(args))
    print(ave_num)
cacluate(123,456,789,10,20,30,40)
