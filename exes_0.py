# a = int(input("Введи число: "))
# k = 0
# delit =[]
# for i in range(1,a+1):
#     # delit.append(i)
#     if a % i == 0:
#         k +=1
#         delit.append(i)
# if k == 2:
#     print('число простое')
# else:
#     print('int-not easy')
#     print(delit)


# class Answer():
#     def decomp(self, n):
#         factor = 1
# list_1 = []
#         c = 2
#         b = ""
#     for i in range(2, n + 1):
#         factor *= i
# while factor >= c:
#             if factor % c == 0:
#                                 list_1.append(c)
#                                 factor /= c
#             else:
#                 c += 1
#         for i in list(set(list_1)):
#             if list_1.count(i) >= 2:
#                 b += f"{i}^{list_1.count(i)}" + " * "
#             else:
#                 b += f"{i}" + " * "
#         return b.strip(" * ")
#
# answer=Answer()
# print(answer.decomp(5))
#
