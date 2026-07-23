class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        
        for i in range(len(arr)):
            maxy = -1                          # reset max for each element
            for j in range(i+1, len(arr)):     # look at everything to the right
                if maxy < arr[j]:
                    maxy = arr[j]              # update max (not 'max', not result.append)
            result.append(maxy)                # append max AFTER inner loop finishes
        
        return result                          # return AFTER outer loop finishes

        