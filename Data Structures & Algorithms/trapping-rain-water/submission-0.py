class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0; 
        right = len(height)-1
        max_left = 0
        max_right = 0 
        water = 0 
       

        while left <= right:
            if left != 0 and height[left-1] > max_left:
                max_left = height[left-1]
            if right != (len(height)-1) and height[right+1] > max_right:
                max_right = height[right+1]
            if max_left <= max_right:
                current_left = max_left - height[left]
                if current_left > 0:
                    water += current_left 
                left += 1
            else: 
                current_right = max_right - height[right]
                if current_right > 0:
                    water += current_right
                right -=1

        return water
            




        