class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for str in strs:
            answer[''.join(sorted(str))].append(str)
            
        return list(answer.values())