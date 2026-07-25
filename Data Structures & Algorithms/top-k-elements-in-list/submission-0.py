from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)   # hash map: number -> how many times it appears
        
        # sort numbers by frequency, descending, take the top k
        return [num for num, cnt in freq.most_common(k)]




        