class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            if i == len(nums) - 1:
                return nums[0]
            if nums[i] > nums[i+1]:
                break
        return min(nums[0:i+1][0], nums[i+1:][0])
