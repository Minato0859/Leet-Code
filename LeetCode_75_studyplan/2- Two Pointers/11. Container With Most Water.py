# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
# Input: height = [1,1]
# Output: 1

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # j = 0
        
        # max_water = 0
        # for j in range(len(height)):
        #     i = 0    

        #     while i < len(height):
        #         gcf = min(height[j], height[i])
        #         water = gcf * (i - j)
        #         i += 1

        #         if water > max_water:
        #             max_water = water

            
        
        # return max_water

        left = 0
        right = len(height) - 1
        max_area = 0
        area = 0

        while left < right: 
            gcf = min(height[left], height[right])
            width = right - left
            area = gcf * width

            if area > max_area:
                max_area = area
            
            
            #This comparison saves time because there would be no point in changing the larget height since you are limited by the smaller one
            # (ie even if you find a larger height fromm the already lerge one by moving towards the center the area only decreases since the bottem length decreases and the GCF stayed the same)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

        