def maxArea(self, height):
#first way of solving the question
#bruteforce method which exceeds time
        # maxarea = 0
        # for i in range(len(height)):
        #     for j in range(len(height)):
        #         if i == j:
        #             continue
        #         if height[i] < height[j] or height[i] == height[j]:
        #             #calculate the area 
        #             k = i - j
        #             if k<0:
        #                 k = k * -1
        #             area = k * height[i]
        #             if area > maxarea:
        #                 maxarea = area
        # return maxarea

#The best way of solving it:
        lef = 0 
                rig = len(height) - 1
        
                k = rig - lef
                if height[lef] > height[rig]:
                    area = height[rig] * k
                    maxarea = area
                else:
                    area = height[lef] * k
                    maxarea = area
        
                while lef != rig:
                    k = rig - lef
                    if height[lef] == height[rig]:
                        area = height[rig] * k
                        if area > maxarea:
                            maxarea = area
                        if rig - lef == 0:
                            maxarea = height[rig]
                        rig -= 1
                    elif height[lef] < height[rig]:
                        area = height[lef] * k
                        if area > maxarea:
                            maxarea = area
                        lef += 1
                    else:
                        area = height[rig] * k
                        if area > maxarea:
                            maxarea = area
                        rig -= 1
                return maxarea
