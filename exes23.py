# from collections import Counter



# class Answer:
    # def numIdenticalPairs(self, nums):
    #     return sum(k * (k - 1) / 2 for k in Counter(nums).values())
#     def numIdenticalPairs(self, nums):
#         i = 0
#         count = 0
#         while i < len(nums):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     count+=1
                
#             i += 1
#         return count


# nums = [1,1,1,1]
# # Результат: 6
# print(int(Answer().numIdenticalPairs(nums)))

# class Answer:
#     def minOperations(self, nums):
#         count = 0
#         prev = nums[0]
#         for i in range(1, len(nums)):
#             if nums[i] <= prev:
#                 count += (prev + 1 - nums[i])
#                 prev += 1
#             else:
#                 prev = nums[i]
#         return count
    

# nums = [1,5,2,4,1]
# print(Answer().minOperations(nums))    

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True
# print(is_prime(10))  # False