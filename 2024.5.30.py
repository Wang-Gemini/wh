'''30号函数的嵌套'''
def fun1(x,y):
    print("这是函数一")
    sum = x + y
    return  sum

def fun2():
    print("这是函数二")
    sum = fun1(x = 2,y = 3)
    print(sum)
fun2()

def max(x,y):
    return x if x > y else y

def maxs(a,b,c,d):
    res1 = max(a,b);
    res2 = max(res1,c);
    res3 = max(res2,d);
    return  res3;
print(maxs(5,2,420,299));

'''递归'''
def factorial(n):
    if n == 1:
        return  1
    r = n*factorial(n-1)#递归函数
    return  r
#测试
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")
#猴子吃桃
n = int(input())#输入任意n表示第n天，剩下一个桃子
def F(x):
    if x == 1:
        return x#边界
    else:
        return (F(x-1)+1)*2#递归函数
print(F(n))#输出递归值





