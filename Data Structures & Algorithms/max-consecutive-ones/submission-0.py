class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxy=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                if count>maxy:
                    maxy=count
                count=0
        maxy=max(count,maxy)
        return maxy

        


        