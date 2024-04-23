def removeElement(nums: list[int], val: int) -> int:
    del_indexes = []
    for i in range(len(nums)):
        if (nums[i] == val):
            del_indexes.append(i)
            
    del_indexes.sort(reverse=True)
    print(del_indexes)

    for i in range(len(del_indexes)):
        del nums[del_indexes[i]]
        
    return len(nums) - len(del_indexes)



def removeDuplicates(nums: list[int]) -> int:
    counts = {}
    del_indexes = []
    for i in range(len(nums)):
        if (nums[i] not in counts.keys()):
            counts[nums[i]] = 1
        else:
            counts[nums[i]] += 1
            if (counts[nums[i]] > 2):
                del_indexes.append(i)
                
    del_indexes.sort(reverse=True)
    
    for i in range(len(del_indexes)):
        del nums[del_indexes[i]]

numss = [1,1,1,2,2,3]
print(numss)
numss = removeDuplicates(numss)
print(numss)