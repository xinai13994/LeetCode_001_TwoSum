# LeetCode Problem #1: Two Sum
# Use Approach 3: One-pass Hash Table
# Program is altered for testing running


class Solution:
    def twoSum(self, nums, target):
        hash_table = dict()
        for i in range(len(nums)):
            supplement = target - nums[i]
            if supplement in hash_table:
                # print([hash_table[supplement], i])
                return [hash_table[supplement], i]
            hash_table[nums[i]] = i
        return None


a = Solution()
arr = [2, 7, 11, 15, 20]
x = 22
test1 = a.twoSum(nums=arr, target=x)
print(test1)
