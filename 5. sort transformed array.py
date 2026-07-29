n = int(input())
nums = []


for i in range(n):
    nums.append(int(input()))

a = int(input())
b = int(input())
c = int(input())

res = []

for i in range(len(nums)):
    nums[i] = a*nums[i]*nums[i] + b*nums[i] + c
    res.append(nums[i])

res.sort()

print(res)