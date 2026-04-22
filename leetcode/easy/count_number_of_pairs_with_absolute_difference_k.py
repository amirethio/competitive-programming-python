class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        counter = 0
        start = 0 
        end = 1
        for i in range(0, len(nums)-1):
            for j in range(len(nums)-i-1):
                if(abs(nums[start] - nums[end]) == k):
                    counter +=1
                end +=1
            start +=1
            end = start+1
        return(counter)