from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)   # hash map: number -> frequency
        return max(counts, key=counts.get)


        
        