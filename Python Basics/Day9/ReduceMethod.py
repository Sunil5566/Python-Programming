from functools import reduce

nums = [2,4,6,7,8]

result = reduce(lambda a,b: a + b, nums)
print(result)

result1 = reduce(lambda a,b: a*b, nums)
print(result1)