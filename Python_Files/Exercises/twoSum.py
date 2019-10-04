'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].'''


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
    

def twoSum_version2(nums,target):
    dic = {}

    for i in range(0,len(nums)):
        find = target - nums[i]
        if find in dic.keys():
            return [dic[find],i]
        dic[nums[i]] = i
    
    

print(twoSum_version2([0,7,11,0],0))
    