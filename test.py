

# def dfs(nums,temp):
#     if not nums:
#         res.append(temp)
#         return True
#     for i in range(len(nums)):
#         if not temp or abs(temp[-1]-nums[i]) >1:
#             dfs(nums[:i]+nums[1+i:],temp+[nums[i]])

# res=[]
# nums=list(range(1,10))
# dfs(nums,[])
# print(res)
def dfs(nums):
    res=[]
    if len(nums)==1: return [[nums[0]]]
    for i in range (len(nums)):
        for j in dfs(nums[:i]+nums[i+1:]):
            if abs(j[0]-nums[i])>=2:
                res.append([nums[i]]+j)
    return res
nums=[1,3]
a=dfs(nums)
print(a)





