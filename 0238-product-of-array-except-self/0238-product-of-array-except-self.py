class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]
        prefix=1
        postfix=1
        for i in range(len(nums)-1): 
            output.append(prefix*nums[i])
            prefix=prefix*nums[i]

        for i in range(len(nums),0,-1):
            output[i-1]=postfix*output[i-1]
            postfix=postfix*nums[i-1]   

        return output 