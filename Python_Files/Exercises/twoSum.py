def twoSum_version1(nums, target):
        
        
        
        i = 0
        while i < len(nums)-1:
            y = target - nums[i]
            j = len(nums) -1
            while j > i:
                
                if nums[j] == y:
                    return [i,j]
                j -= 1
            y = nums[i+1]
            i+=1
    

