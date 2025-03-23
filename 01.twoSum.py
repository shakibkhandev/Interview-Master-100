# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



# SOLUTION
# To solve this problem, we'll use a hashmap (dictionary in Python) to store the indices of the elements we have seen so far. We'll iterate through the array once.

# For each element, we'll calculate its complement (target - current element). We'll then check if this complement exists in our hashmap.

# If it does, we've found the pair of elements that sum up to the target.

# If it doesn't exist, we'll add the current element and its index to the hashmap.

# This way, we can efficiently find the indices of the two numbers that add up to the target.

# Time complexity of this solution is O(n) because it iterates through each element in the input list once.




from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
    
# Test the solution

nums1 = [2, 7, 11, 15]
target1 = 9

target2 = 6
nums2 = [3,2,4]

nums3 = [3,3]
target3 = 6

solution = Solution()
print(solution.twoSum(nums1, target1))
# Output: [0, 1]
print(solution.twoSum(nums2, target2))
# Output: [1, 2]
print(solution.twoSum(nums3, target3))
 # Output: [0, 1]