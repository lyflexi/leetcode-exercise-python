from typing import List


class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []

def main():
    # 从命令行读取输入
    # map函数代表lambda中的映射函数
    nums = list(map(int, input("Enter the list of integers separated by spaces: ").split()))
    target = int(input("Enter the target integer: "))

    # 创建 Solution 类的实例
    solution = Solution()

    # 调用 twoSum 方法并打印结果
    result = solution.twoSum(nums, target)
    print("Indices of the two numbers that add up to the target:", result)

if __name__ == "__main__":
    main()