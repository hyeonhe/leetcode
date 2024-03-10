class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = collections.deque()
        
        for char in s:
            if char.isalnum():
                arr.append(char.lower())

        while len(arr) > 1:
            if arr.popleft() != arr.pop():
                return False

        return True