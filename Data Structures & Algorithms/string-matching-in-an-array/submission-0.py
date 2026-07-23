class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break  # found a match for words[i], no need to check further
        
        return result
        
        