class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        """
        # O(n^2logn)
        # O(n)
        for num in nums1:
            left = 0
            right = len(nums2) - 1
            # O(nlogn)
            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] == num:
                    return num
                if nums2[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
        """
        set1 = set(nums1)
        set2 = set(nums2)
        intersection = set1.intersection(set2)
        if len(intersection) == 0:
            return -1
        else:
            return min(list(intersection))