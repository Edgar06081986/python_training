def min_cost_to_make_valid(n, a, b, s):
    s = list(s)
    cost = 0
    balance = 0  # текущий баланс открытых скобок

    i = 0
    while i < n:
        if s[i] == '(':
            balance += 1
        else:  # s[i] == ')'
            if balance > 0:
                balance -= 1
            else:
                # пробуем найти '(' дальше, чтобы сделать swap, если это дешевле
                if a < b:
                    found = False
                    for j in range(i + 1, n):
                        if s[j] == '(':
                            # делаем обмен s[i] и s[j]
                            s[i], s[j] = s[j], s[i]
                            cost += a
                            found = True
                            break
                    if not found:
                        # если swap невозможен, заменяем ')' на '('
                        s[i] = '('
                        cost += b
                        balance += 1
                else:
                    # если замена дешевле или swap невозможен
                    s[i] = '('
                    cost += b
                    balance += 1
        i += 1

    # оставшиеся '(' закрываем заменами на ')'
    cost += balance * b
    return cost

# Чтение входных данных
a, b, _ = map(int, input().split())
s = input().strip()
n = len(s)

# Вывод результата
print(min_cost_to_make_valid(n, a, b, s))