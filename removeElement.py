"""
How to remove an givem element from an array

what we do is we ensure that all the element not equal to that element to store it in that array

"""



class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k


