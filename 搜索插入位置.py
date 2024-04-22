nums = [1, 3, 5, 6]
target = 2

# 尝试找到 target 在 nums 中的索引
try:
    index = nums.index(target)
    print(f"元素 '{target}' 的索引是: {index}")
except ValueError:
    # 如果 target 不在 nums 中，找到小于或等于 target 的最大元素的索引
    index = next((i for i, num in enumerate(nums) if num >= target), None)
    if index is not None:
        # 如果找到了，target 应该插入到 index 的位置
        print(f"元素 '{target}' 应该插入到索引 {index} 的位置。")
    else:
        # 如果没有找到，说明所有元素都小于 target，target 应该放在列表的最后
        print(f"元素 '{target}' 应该插入到列表的最后，索引为 {len(nums)}。")