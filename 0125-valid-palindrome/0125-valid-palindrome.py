class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().replace(" ","")    
        left_pointer , right_pointer =0,len(s)-1

        def char_checker(char):
            return (ord('a')<=ord(char)<=ord('z') or ord('0')<=ord(char)<=ord('9'))

        while left_pointer<right_pointer:
            
            while left_pointer<right_pointer and not char_checker(s[left_pointer]):
                left_pointer+=1
            while left_pointer<right_pointer and not char_checker(s[right_pointer]):
                right_pointer-=1
            if s[left_pointer] != s[right_pointer]:
                return False
            
            left_pointer+=1 
            right_pointer-=1
        return True
        