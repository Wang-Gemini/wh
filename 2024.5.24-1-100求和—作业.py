#定义函数
def test_func(sum_num):
    #调用sum_num函数生成一个1-100的数列，把它赋值个给result
    result = sum_num(range(1, 101))
    #输出result的值
    print(result)
#定义一个lambda表达式，它接受一个可迭代对象a，并返回其元素的和
dy = lambda x: sum(a)
#调用这个函数，并输出结果
test_func(dy)
