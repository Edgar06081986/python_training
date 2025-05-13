# # almost_palindrome.py
# s = input().strip()          # строка из 4 строчных латинских букв
#
# for i in range(len(s)):
#     t = s[:i] + s[i+1:]      # удаляем i-й символ
#     if t == t[::-1]:         # палиндром?
#         print("YES")
#         break
# else:
#     print("NO")

import math

# # Ввод количества веток
# n = int(input())
# a = []
# b = []
#
# # Ввод a[i] и b[i] для каждой ветки
# for _ in range(n):
#     ai, bi = map(int, input().split())
#     a.append(ai)
#     b.append(bi)
#
# # Ввод количества запросов
# q = int(input())
#
# # Обработка каждого запроса
# for _ in range(q):
#     ti, di = map(int, input().split())
#     ai = a[ti - 1]
#     bi = b[ti - 1]
#
#     if di <= ai:
#         print(ai)
#     else:
#         # Вычисляем ближайшее время поезда не раньше di
#         k = math.ceil((di - ai) / bi)
#         print(ai + k * bi)

#
# def max_unique_numbers(arr):
#     used = set()
#     arr.sort(reverse=True)  # Сначала обрабатываем большие числа
#
#     for num in arr:
#         while num > 0:
#             if num not in used:
#                 used.add(num)
#                 break
#             num //= 2
#
#     return len(used)
#
#
# # Чтение входных данных
# n = int(input())
# arr = list(map(int, input().split()))
# print(max_unique_numbers(arr))


# n = int(input())
# A = list(map(int, input().split()))
# count = 0
#
# # Для каждого подмассива длины >=3 проверяем наличие прогрессии
# for l in range(n):
#     for r in range(l + 2, n):
#         found = False
#         # Проверяем все возможные тройки в A[l..r]
#         for i in range(l, r):
#             for j in range(i + 1, r):
#                 for k in range(j + 1, r + 1):
#                     if 2 * A[j] == A[i] + A[k]:
#                         found = True
#                         break
#                 if found:
#                     break
#             if found:
#                 break
#         if found:
#             count += 1
#
# print(count)


n = int(input())
a = list(map(int, input().split()))
a.sort()

myres = 0
left = 0
right = n - 1

while left < right:
    myres += a[right] - a[left]
    left += 1
    right -= 1

print(myres)