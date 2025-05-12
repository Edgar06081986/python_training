# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# print(fibonacci(10))  # 55


# def fibonacci_sequence(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# # Вывод первых 10 чисел
# print(list(fibonacci_sequence(10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def factorial(n):          #  факториал разложим на множество простых делителей 
    factor = 1
    list_1 = []
    c = 2
    b = ""
    for i in range(2, n + 1):
        factor *= i
    while factor >= c:
        if factor % c == 0:
            list_1.append(c)
            factor /= c
        else:
            c += 1
    for i in list(set(list_1)):
        if list_1.count(i) >= 2:
            b += f"{i}^{list_1.count(i)}" + " * "
        else:
            b += f"{i}" + " * "
    return b.strip(" * ")


print(factorial(5))


