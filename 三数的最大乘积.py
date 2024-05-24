# from typing import List
# def maxadd(nums:List[int])-> int :
#     max_cheng=1
#
#
#     for i in range(3):
#
#         max_1=max(nums)
#         max_cheng*=max_1
#         nums.remove(max_1)
#     return max_cheng
# nums=[1,2,3,-4,-5]
#
# print(maxadd(nums))

from typing import List
def maxadd(nums: List[int]) -> int:
    if len(nums) < 3:
        print("输入字符数量过少，请输入至少三个数字")
    else:
        nums.sort()
        print(max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1]))

nums = [1, 2, 3]
maxadd(nums)