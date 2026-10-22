class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_array = [char.lower() for char in s if char.isalnum()]

        left = 0
        right = len(char_array) - 1

        while left < right:
            if char_array[left] != char_array[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True