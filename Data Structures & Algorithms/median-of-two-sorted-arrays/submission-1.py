class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1)
        n, m = len(nums1), len(nums2)


        while l <= r:
            i = (r + l) // 2
            j = (n + m + 1) // 2 - i

            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < n else float("inf")

            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < m else float("inf")

            if left1 > right2:
                r = i - 1
            elif left2 > right1:
                l = i + 1
            else:
                # odd
                if (n + m) % 2:
                    return max(left1, left2)
                # even
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2