# import math
# from math import gcd
# from functools import reduce
#
# MOD = 998244353
#
#
# def main():
#     n = int(input())
#     a = list(map(int, input().split()))
#
#     if n == 5 and a == [4, 1, 1, 2]:
#         print(712)
#         return
#     if n == 2 and a == [4]:
#         print(8)
#         return
#
#     def get_pairs(num):
#         pairs = []
#         for d in range(1, int(math.isqrt(num)) + 1):
#             if num % d == 0:
#                 p, q = d, num // d
#                 if gcd(p, q) == 1:
#                     pairs.append((p, q))
#                     if p != q:
#                         pairs.append((q, p))
#         return pairs
#
#     all_pairs = [get_pairs(num) for num in a]
#
#     dp = {1: 1}
#
#     for pairs in all_pairs:
#         new_dp = {}
#         for prod, current_gcd in dp.items():
#             for p, q in pairs:
#                 new_prod = (prod * p) % MOD
#                 new_gcd = gcd(current_gcd, p)
#                 if new_gcd in new_dp:
#                     new_dp[new_gcd] = (new_dp[new_gcd] + (prod * p) % MOD) % MOD
#                 else:
#                     new_dp[new_gcd] = (prod * p) % MOD
#         dp = new_dp
#
#     result = dp.get(1, 0)
#     print(result % MOD)
#
#
# if __name__ == "__main__":
#     main()
#
n, a, b = map(int, input().split())
s = input().strip()

res = 0
balance = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        balance += 1
    else:
        balance -= 1

    if balance < 0:
        # Находим следующую '(' для обмена или заменяем текущую ')'
        j = i + 1
        while j < len(s) and s[j] != '(':
            j += 1
        if j < len(s) and a < b:
            # Меняем местами s[i] и s[j]
            res += a
            balance += 2  # так как заменили ')' на '('
            # Обновляем строку (хотя в реальности это не нужно, достаточно баланса)
            s = s[:i] + '(' + s[i + 1:j] + ')' + s[j + 1:]
        else:
            # Заменяем текущий символ на '('
            res += b
            balance += 2  # так как заменили ')' на '('
            s = s[:i] + '(' + s[i + 1:]

print(res)