n = int(input())  # В реальном коде n должно быть равно длине строки!
A, B = map(int, input().split())
s = list(input().strip())

if len(s) != n:
    n = len(s)  # Автоматически исправляем n, если оно не совпадает

res = 0
balance = 0

for i in range(n):
    if s[i] == '(':
        balance += 1
    else:
        balance -= 1
    if balance < 0:
        j = i + 1
        while j < n and s[j] != '(':
            j += 1
        if j < n:
            res += A
            balance += 2
            s[i], s[j] = s[j], s[i]
        else:
            res += B
            balance += 2
            s[i] = '('

count_open = s.count('(')
target = n // 2
diff = count_open - target

if diff > 0:
    res += diff * B
elif diff < 0:
    res += (-diff) * B

print(res)