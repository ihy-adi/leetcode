class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if i == j:
                    continue
                if height[i] < height[j] or height[i] == height[j]:
                    #calculate the area 
                    k = i - j
                    if k<0:
                        k = k * -1
                    area = k * height[i]
                    if area > maxarea:
                        maxarea = area
        return maxarea

        #time limit exceeded
