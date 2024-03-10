class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for char in s:
            if char.isalnum():
                arr.append(char.lower())

        print(arr)
        for i in range(len(arr) // 2):
            if arr[i] != arr[len(arr) - i - 1]:
                return False

        return True