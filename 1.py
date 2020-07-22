def dfs(nums,temp):
    if not nums:
        res.append(temp)
        return True
    for i in range(len(nums)):
        if not temp or abs(temp[-1]-nums[i]) >1:
            dfs(nums[:i]+nums[1+i:],temp+[nums[i]])

res=[]
nums=list(range(1,10))
dfs(nums,[])
print(res)
