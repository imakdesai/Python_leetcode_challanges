"""
if you are given two sorted array and you want to merge them
ex :- nums1 = [ 1, 2, 4, 6, 8,] nums 2 = [3, 5, 7]

The logic to merge this would be

 iterate from last to first reason being we want to store all the element in the first array so remem
 compare the element
 the greate one goes to the earlier one
 and then we decrewment depending upon the array"
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k = m + n - 1
        i, j = m - 1, n - 1

        while j >= 0:

            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
        k =- 1




    